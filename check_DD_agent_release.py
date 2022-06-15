#!/usr/bin/env python

import requests

# Script to check latest release of DD host agent

# Release uri

dd_uri = "https://api.github.com/repos/DataDog/datadog-agent/releases/latest"

# make a get request to get the latest release details

headers = "Accept: application/vnd.github.v3+json" 

res = requests.get(dd_uri)

print(res.json())