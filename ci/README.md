# CI

## Artifactory

The following commands were used to configure CI with Travis (one-time setup).

Access travis:

```shell
gem install travis --no-rdoc --no-ri
travis login -X -g <...>
```

Do actual setup:

```shell
travis env set ART_URL <...>
travis env set ART_USERNAME <...>
travis env set ART_API_KEY <...>
```

`ART_URL` should resemble `https://na.artifactory.swg-devops.com/artifactory/api/pypi/apset-pypi-local`

Keep `@` as `@` in `ART_USERNAME`

## Slack

The value for `notifications/slack/secure` is obtained by running the following
command.

```sh
travis encrypt "<SLACK_TEAM_SUB_DOMAIN>:<SLACK_TOKEN>"
```
