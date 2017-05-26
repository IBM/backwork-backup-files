"""File backup module for Monsoon
"""

from setuptools import setup, find_packages
from os import path

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="monsoon-backup-files",
    version="0.1.0",
    description="Monsoon plug-in for file backups.",
    long_description=LONG_DESCRIPTION,
    url="https://github.ibm.com/apset/monsoon-backup-files",
    author="Leons Petrazickis",
    author_email="leonsp@ca.ibm.com",
    license="IBM",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Utilities"
    ],
    packages=find_packages(),
    install_requires=[
        "monsoon>=0.1.0"
    ],
    entry_points={
        "monsoon.backups": [
            "files=files:FilesBackup"
        ]
    }
)
