from setuptools import setup, find_packages

__author__ = "Manuel Huber"
__version__ = "0.1.0"

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
    ]
)
