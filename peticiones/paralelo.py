#!/usr/bin/env python

import requests
import threading

urls = [
    'https://www.reddit.com/r/python',
    'https://www.reddit.com/r/programming',
    'https://www.reddit.com/r/linux',
] * 5

def worker(url):
    requests.get(url)

threads = []
for url in urls:
    t = threading.Thread(target=worker, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()