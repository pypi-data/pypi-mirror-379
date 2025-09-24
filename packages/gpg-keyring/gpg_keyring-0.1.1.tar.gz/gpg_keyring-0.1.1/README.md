GPG Keyring
===========

Simple keyring implementation using `gpg` to store encrypted credentials on the file system.

# Setup

1. Install this package (f.e. into a virtual environment)
2. Create the file as specified by `keyring diagnose`. The output should look similar to this:

        config path: <HOME-FOLDER>/.config/python_keyring/keyringrc.cfg
        data root: <HOME-FOLDER>/.local/share/python_keyring

3. Use this snippet to configure this keyring backend as default:

        [backend]
        default-keyring=gpg_keyring.GpgKeyring

4. Configure your e-mail address in the file `~/.gpg_keyring/gpg_keyring.conf`:


        [settings]
        email = john.doe@domain.com

Now you should be able to use the `gpg_keyring` backend using commands like this:

- `keyring set <service> <username>` to set a password
- `keyring get <service> <username>` to retrieve the password
- `keyring del <service> <username>` to delete an entry

# Internals

Credentials and local settings are all stored in your home directory in the directory  `~/.gpg_keyring/`:

- `gpg_keyring.conf`: configuration file for this plugin
- `<SHA256-hash>`: credentials for the service. The service name is turned into a SAH-256 hash and used to as the name of the file containing the credentials.

The content of the credentials files is a base64 encoded cipher text of the following json structure:

        {
            "username": "<username>",
            "password": "<password>"
        }

... the user name `<username>` and the password `<password>` previously set via `keyring set <service> <username>` with the password `<password>` provided via `stdin`.
