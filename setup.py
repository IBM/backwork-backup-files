from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name="monsoon-backup-filesystem",
    version="0.1.0",
    description="Monsoon plug-in for filesystem backups.",
    long_description=long_description,
    url="https://github.ibm.com/apset/monsoon-backup-filesystem",
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
            "filesystem=filesystem:FileSystemBackup"
        ]
    }
)
