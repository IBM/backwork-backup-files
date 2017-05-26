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

# Log into Artifactory
curl -su "$ART_USERNAME:$ART_API_KEY" "$ART_URL/api/v1/api_key.yaml" > ~/.gem/credentials
chmod 0600 ~/.gem/credentials

gem push companion_cube*.gem --host "$ART_URL"#!/usr/bin/env bash
