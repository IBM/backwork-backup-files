# -*- coding: utf-8 -*-
"""File System Backup module for Monsoon
"""

import logging
import subprocess

LOGGER = logging.getLogger(__name__)


class FileSystemBackup(object):
    """Backup a filesystem location.

    It uses `tar -cz` and gzips the output. You can use any of the
    arguments supported by `tar`. Add a list of files and
    directories you want backed up as the last thing in the line.
    Use `tar --help` for more information.
    """
    command = "filesystem"

    def __init__(self, args, extra):
        """Initialize a backup command given the arguments passed to CLI"""

        self.args = args
        self.extra = extra

    @classmethod
    def parse_args(cls, subparsers):
        """Create the `filesystem` subparser for the `backup` command.
        :param subparsers: Main argument parser
        """
        fs_parser = subparsers.add_parser(cls.command, description=cls.__doc__)

        fs_parser.add_argument("-f", "--file", required=True,
                               help="output gzipped file path")

    def backup(self):
        """Backup a filesystem location."""
        LOGGER.info("starting filesystem backup...")

        try:
            tar_cmd = ["tar", "-cz", "-f", self.args.file] + self.extra
            subprocess.Popen(tar_cmd)
            LOGGER.info("filesystem backup complete")
        except Exception as error:
            LOGGER.error("Failed to backup filesystem location")
            raise error
