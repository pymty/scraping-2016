#!/usr/bin/env python

import grequests

urls = [
    'https://www.reddit.com/r/python',
    'https://www.reddit.com/r/programming',
    'https://www.reddit.com/r/linux',
] * 5

rs = (grequests.get(u) for u in urls)
grequests.map(rs)
