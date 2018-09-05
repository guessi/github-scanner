#!/usr/bin/env python

import json
import requests
import sys

from prettytable import PrettyTable


def check_orgs_existence(org_name):
    # TODO: public repositories paging
    API = 'https://api.github.com/orgs/' + org_name
    API += '/repos?type=public&per_page=100&page=1'

    res = requests.get(API)
    if res.status_code >= 200 and res.status_code < 300:
        repo_json = json.loads(res.content)
    elif res.status_code >= 400 and res.status_code < 500:
        if "API rate limit" in res.text:
            print("Oops... hit GitHub API rate limit, please try again later")
        sys.exit(1)
    else:
        print('Oops... unexpected return while checking orgs existence')
        sys.exit(1)

    return repo_json


def report(org, repos, isFork):
    pt = PrettyTable()
    pt.field_names = [
        'Repository',
        'Language',
        'License',
        'Forks',
    ]

    pt.align['Repository'] = 'l'
    pt.align['License'] = 'r'
    pt.align['Language'] = 'r'
    pt.align['Forks'] = 'l'

    count = 0
    for repo in repos:
        if isFork == repo['fork']:
            pt.add_row([
                repo['name'],
                repo['language'],
                (repo['license']['spdx_id'] if repo['license'] else "N/A"),
                repo['forks'],
            ])
            count += 1

    return str(pt), count


def post_slack(slack_hook, org, msg, count, is_fork):
    payload = {
        "attachments": [
            {
                "title":
                    "GitHub - Public Repositories under {0} (Type: {1})"
                    .format(org, "Fork" if is_fork else "NotFork"),
                "pretext":
                    "Found {0} public repos :scream:".format(str(count)),
                "text":
                    "```{0}```".format(msg),
                "color":
                    "#F35A00"
            }
        ]
    }

    requests.post(slack_hook, data=json.dumps(payload), timeout=10)
