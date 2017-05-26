#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

#gem build companion_cube.gemspec

echo \
"[distutils]
index-servers = local
[local]
repository: ${ART_PY_URL:?}
username: ${ART_USERNAME:?}
password: ${ART_API_KEY:?}" > ~/.pypirc

python setup.py sdist upload -r local
