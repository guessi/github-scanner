#!/usr/bin/env python

import argparse
import json
import sys

from utils import check_orgs_existence, report, post_slack


def main(org_name, slack_hook, console_output):
    try:
        repo_json = check_orgs_existence(org_name)
    except Exception:
        print('Oops... something went wrong')
        sys.exit(1)

    # check forked repositories
    msg, count = report(org_name, repo_json, True)
    post_slack(slack_hook, org_name, msg, count, True)
    if console_output:
        print("Type: Fork")
        print(msg)

    # check non-fork repositories
    msg, count = report(org_name, repo_json, False)
    post_slack(slack_hook, org_name, msg, count, False)
    if console_output:
        print("Type: NotFork")
        print(msg)


if __name__ == "__main__":
    description = '''
    Public GitHub repositories analyser, and post the scan results to slack
    '''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-o', dest='org_name', type=str,
                        help='GitHub organization name',
                        required=True)
    parser.add_argument('-s', dest='slack_hook', type=str,
                        help='Slack incoming webhook URL',
                        required=True)
    parser.add_argument('-v', dest='console_output',
                        action='store_true',
                        required=False)
    args = parser.parse_args()

    main(args.org_name, args.slack_hook, args.console_output)
