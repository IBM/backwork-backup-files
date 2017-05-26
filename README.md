# monsoon-backup-filesystem
Add support for filesystem backups on [`monsoon`](https://github.ibm.com/apset/monsoon).

## Requirements
This plug-in is build on top of [`tar`](https://linux.die.net/man/1/tar).

## Installing
You can use `pip` to install this plug-in from Artifactory.

First you will need to configure your pip client by creating or editing the
`~/.pip/pip.conf` file to look like the example below.

**Note:** Remember to change `@` into `%40` in your username!

```
[global]
index-url = https://pypi.python.org/simple
extra-index-url = https://<USERNAME>:<API KEY>@na.artifactory.swg-devops.com/artifactory/api/pypi/apset-pypi-local/simple
```

After that you should be able to run
```sh
$ pip install monsoon-backup-fileystem
```

Alternatively, you can install it directly from GHE:
```sh
$ pip install git+ssh://git@github.ibm.com/apset/monsoon-backup-filesystem
```

## Using
After installing the plug-in you will be able to use the `backup filesystem` command
on `monsoon`.

```sh
$ monsoon backup filesystem -h
usage: monsoon backup filesystem [-h] -f FILE

Backup a filesystem location. It uses `tar -cz` and gzips the output. You can
use any of the arguments supported by `tar`. Add a list of files and
directories you want backed up as the last thing in the line. Use `tar --help`
for more information.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  output gzipped file path
```

You can pass any option that you would normally use on `mysqldump`:

```sh
$ monsoon backup filesystem -f foo.tgz --verbose /tmp /var/log
```

As shown in the `--help` message, there is one required arguments you
must use in your backup process.

`-f FILE` or `--file FILE` will save the output of `tar` into a
file.

**Important:** There is a conflict with the `-h` argument since it is reserved
for the help/usage message. Use `--dereference` to follow symlinks.
