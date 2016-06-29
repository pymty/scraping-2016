#!/usr/bin/env python

import requests

urls = [
    'https://www.reddit.com/r/python',
    'https://www.reddit.com/r/programming',
    'https://www.reddit.com/r/linux',
] * 5

for url in urls:
    requests.get(url)