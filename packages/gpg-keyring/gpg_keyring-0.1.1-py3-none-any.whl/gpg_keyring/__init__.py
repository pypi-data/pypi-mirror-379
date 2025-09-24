import os
import sys
import base64
import fcntl
import logging
import hashlib
import configparser
import contextlib
import json
from pathlib import Path
from keyring.backend import KeyringBackend
from keyring.errors import PasswordDeleteError, PasswordSetError
from keyring.credentials import SimpleCredential
from getpass import getpass


if os.environ.get('GPG_KEYRING_SETUP_LOGGING'):
    _log_format = "{asctime:<15} : {name:<15} : {threadName:>15} : {levelname:>8} : {message}"
    _main_log_handler = logging.StreamHandler(sys.stderr)
    logging.basicConfig(format=_log_format,
                        style='{',
                        handlers=[_main_log_handler],
                        level=logging.INFO)

_env_log_level = os.environ.get('GPG_KEYRING_LOG')
if _env_log_level:
    logging.root.setLevel(_env_log_level.upper())

_log = logging.getLogger(__name__)


class GpgKeyring(KeyringBackend):
    """Simple file based keyring using gpg"""

    priority = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._config_dir = _ensure_config_dir()
        self._secret = Secret()
        self._log = logging.getLogger(__name__)

    def get_credential(self, service, username):
        filename = _get_filename_hash(service)
        filepath = self._config_dir / filename
        if not filepath.exists():
            self._log.info("No password stored for service '%s' and user '%s' (expected a file '%s')", service, username, str(filepath))
            return None
        self._log.debug("Attempt to retrieve the password for service '%s' and user '%s' from the directory '%s'", service, username, str(filepath))
        with _gpg_keyring_lock_file():
            with open(filepath, 'rb') as f:
                data = f.read()
        ok, data = self._secret.decrypt_base64(data.decode('utf-8'))
        if ok:
            self._log.debug("Succeeded to decode the password for service '%s' and user '%s'", service, username)
            obj = json.loads(data.decode('utf-8'))
            assert 'username' in obj, "username must exist"
            assert 'password' in obj, "password must exist"
            return SimpleCredential(obj['username'], obj['password'])
        else:
            self._log.error("Failed to decode the password for service '%s' and user '%s'", service, username)
            return None

    def _set_credential(self, service, username, password):
        filename = _get_filename_hash(service)
        filepath = self._config_dir / filename
        self._log.debug("Attempt to store the password for service '%s' and user '%s' in the directory '%s'", service, username, str(filepath))
        secret = json.dumps({'username': username, 'password': password})
        ok, cipher_data = self._secret.encrypt_base64(secret)
        if not ok:
            self._log.error("Failed to encrypt the password for service '%s' and user '%s'", service, username)
            raise PasswordSetError("Failed to encrypt the password using GPG")
        with _gpg_keyring_lock_file():
            with open(filepath, 'wb') as f:
                f.write(cipher_data.encode('utf-8'))
        self._log.debug("Succeeded to store the password for service '%s' and user '%s'", service, username)

    def get_password(self, service, username):
        obj = self.get_credential(service, username)
        if obj is None:
            return None
        else:
            return obj.password

    def set_password(self, service, username, password):
        self._set_credential(service, username, password)

    def delete_password(self, service, username):
        filename = _get_filename_hash(service)
        filepath = self._config_dir / filename
        if not filepath.exists():
            self._log.info("No password stored for service '%s' and user '%s' (expected a file '%s')", service, username, str(filepath))
            raise PasswordDeleteError("Password not found")
        with _gpg_keyring_lock_file():
            self._log.debug("Attempt to delete the password for service '%s' and user '%s' (file: '%s')", service, username, str(filepath))
            os.unlink(filepath)
        self._log.debug("Password for service '%s' and user '%s' successfully deleted (file: '%s')", service, username, str(filepath))


class Secret:
    def __init__(self):
        import gnupg
        self._g = gnupg.GPG()
        config_dir = _ensure_config_dir()
        self._config_file = config_dir / 'gpg_keyring.conf'
        self._cfg = self._parse_config(self._config_file)
        self._log = logging.getLogger(__name__)

    @staticmethod
    def _parse_config(config_file):
        cfg = configparser.ConfigParser()
        cfg['settings'] = {}
        if config_file.exists():
            cfg.read(config_file)
        return cfg

    def _get_email(self):
        if 'email' in self._cfg['settings']:
            return self._cfg['settings']['email']
        else:
            #TODO: Maybe ask for it?
            raise ValueError("No email configured in '%s'" % str(self._config_file))

    def decrypt(self, cipher):
        r = self._g.decrypt(cipher)
        if not r.ok:
            passphrase = getpass()
            r = self._g.decrypt(cipher, passphrase=passphrase)
        return r.ok, r.data

    def decrypt_base64(self, b64_cipher):
        cipher = base64.b64decode(b64_cipher)
        return self.decrypt(cipher)

    def encrypt(self, clear_text):
        email = self._get_email()
        r = self._g.encrypt(clear_text, email, armor=False)
        if not r.ok:
            self._log.debug("Failed to encrypt using the e-mail %s", email)
        return r.ok, r.data

    def encrypt_base64(self, clear_text):
        ok, data = self.encrypt(clear_text)
        if ok:
            return ok, base64.b64encode(data).decode('utf-8')
        else:
            return ok, None


def _ensure_config_dir():
    config_dir = Path.home() / '.gpg_keyring'
    if not config_dir.exists():
        _log.info("Creating a credential store in the directory '%s'", config_dir)
        with _gpg_keyring_lock_file():
            config_dir.mkdir(parents=True)
    return config_dir


def _get_filename_hash(service):
    h = hashlib.sha256()
    h.update(service.encode('utf-8'))
    h.update(b'\0')
    return h.hexdigest()


def _gpg_keyring_lock_file():
    return unix_lock_file("gpg_keyring/gpg_keyring")


@contextlib.contextmanager
def unix_lock_file(unique_path):
        xdg_runtime_dir = os.environ.get('XDG_RUNTIME_DIR')
        assert xdg_runtime_dir is not None, "XDG_RUNTIME_DIR must be set"
        assert os.path.isdir(xdg_runtime_dir), "XDG_RUNTIME_DIR must be a directory"
        lockfile = os.path.join(xdg_runtime_dir, unique_path + '.lock')
        topdir = Path(lockfile).parent
        if not topdir.exists():
            topdir.mkdir(parents=True)
        open_flags = os.O_TRUNC | os.O_RDWR
        if not os.path.exists(lockfile):
            open_flags |= os.O_CREAT
        fd = os.open(lockfile, open_flags)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            try:
                yield
            finally:
                fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)
            os.unlink(lockfile)
