#test

import re
from urllib.parse import urlparse

'''
st = input("Enter test string: ")

match = re.search(r".*https://.+", st)
if match:
    print(match.group())
'''

'''This function detects links with https protocol in the msgs and finds the host/website name'''

def url_grab(st: str):
    match = re.search(r".*(https://|http://).+", st)
    if match:
        url = match.group()
        website = urlparse(url).hostname
        print("Link detected: {}\nWebsite: {}".format(url, website))

url_grab('https://www.youtube.com/watch?v=1Qxy3iSU-vo')
