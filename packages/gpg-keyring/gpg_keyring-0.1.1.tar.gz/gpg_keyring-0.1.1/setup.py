import os
from setuptools import setup, find_packages

__author__ = "Manuel Huber"
__version__ = "0.1.1"


# Add GitHub Actions build: add build ids if not building a release (tag)
if os.environ.get("GITHUB_ACTIONS") == "true":
    build_number = os.environ["GITHUB_RUN_NUMBER"]
    build_attempt = os.environ["GITHUB_RUN_ATTEMPT"]
    ref_type = os.environ.get("GITHUB_REF_TYPE", "??")
    ref_name = os.environ.get("GITHUB_REF_NAME", "")
    if (ref_type == "tag") and ref_name:
        if __version__ != ref_name:
            raise RuntimeError("tag != version: {0}, {1}".format(ref_name, __version__))
    else:
        __version__ = "{0}.{1}.{2}".format(__version__, build_number, build_attempt)


setup_extra = dict()
if os.environ.get("NO_README", "") == "":
    with open('README.md') as f:
        setup_extra['long_description'] = f.read()
    setup_extra['long_description_content_type'] = 'text/markdown'
    setup_extra['setup_requires'] = [
        'setuptools>=38.6.0'
    ]


setup(
    name='gpg-keyring',
    version=__version__,
    description='Simple keyring backend using the file system and GPG to store credentials',
    author=__author__,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: POSIX :: Linux",
    ],
    package_dir={
        '': 'src'
    },
    packages=find_packages(where='./src'),
    include_package_data=True,
    entry_points={
        'keyring.backends': [
            'gpg = gpg_keyring',
        ]
    },
    install_requires=[
        'keyring >= 25.6.0',
        'python-gnupg >= 0.5.2',
    ],
    **setup_extra
)
