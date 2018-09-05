# GitHub Public Repositories Scanner

[![Docker Stars](https://img.shields.io/docker/stars/guessi/github-scanner.svg)](https://hub.docker.com/r/guessi/github-scanner/)
[![Docker Pulls](https://img.shields.io/docker/pulls/guessi/github-scanner.svg)](https://hub.docker.com/r/guessi/github-scanner/)
[![Docker Automated](https://img.shields.io/docker/automated/guessi/github-scanner.svg)](https://hub.docker.com/r/guessi/github-scanner/)

a simple helper tool for scanninag public repositories on GitHub

# Prerequisites

Slack Incoming Webhook - https://api.slack.com/incoming-webhooks

# Usage

    $ pip install -r requirements.txt
    $ ./github-scanner.py -o <org_name> -s <slack_incoming_webhook> [-v]

# Sample Output

### Slack Message Output

![Slack Message](slack.png "Slack Message Output")

# Known Issue, Limitation

Currently, it will only return 100 public repositories

# License

[Apache-2.0](LICENSE)
