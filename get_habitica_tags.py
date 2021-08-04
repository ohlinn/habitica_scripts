#!/usr/bin/env python3

import argparse
import json
import os
import requests
import sys
import emoji_data_python

class Debug(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        import pdb; pdb.set_trace()


# MAIN
parser = argparse.ArgumentParser(description="Dumps your tasks to a file user-tags.json in the current directory")
parser.add_argument('-o', '--outfile',
                    type=argparse.FileType('w'), default="user-tags.json",
                    help='JSON data file (default: user-tags.json)')
parser.add_argument('-u', '--user-id',
                    help='From https://habitica.com/#/options/settings/api\n \
                    default: environment variable HAB_API_USER')
parser.add_argument('-k', '--api-token',
                    help='From https://habitica.com/#/options/settings/api\n \
                    default: environment variable HAB_API_TOKEN')
parser.add_argument('--baseurl',
                    type=str, default="https://habitica.com",
                    help='API server (default: https://habitica.com)')
parser.add_argument('--debug',
                    action=Debug, nargs=0,
                    help=argparse.SUPPRESS)
args = parser.parse_args()
args.baseurl += "/api/v3/"

try:
    if args.user_id is None:
        args.user_id = os.environ['HAB_API_USER']
except KeyError:
    print("User ID must be set by the -u/--user-id option or by setting the environment variable 'HAB_API_USER'")
    sys.exit(1)

try:
    if args.api_token is None:
        args.api_token = os.environ['HAB_API_TOKEN']
except KeyError:
    print("API Token must be set by the -k/--api-token option or by setting the environment variable 'HAB_API_TOKEN'")
    sys.exit(1)


headers = {"x-api-user": args.user_id, "x-api-key": args.api_token, "Content-Type": "application/json"}

#### T A G S ####

reqt = requests.get(args.baseurl + "tags", headers=headers)
                                           
# with open(args.outfile, 'w') as f:  
tags_data = {}
each_tag = []
for tag_entry in reqt.json()['data']:
  tag_info = {}
  tag_info.update({tag_entry['id'] : emoji_data_python.replace_colons(tag_entry['name'])})     
  each_tag.append(tag_info)
tags_data.update({"TAGS": each_tag})

with open('user-tags.json', 'w', encoding='utf8') as json_file:
    json.dump(tags_data, json_file, ensure_ascii=False, separators=(',', ':'), sort_keys=True, indent=3)
