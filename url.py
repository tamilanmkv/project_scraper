#!/bin/env python3

import re
import requests
from bs4 import BeautifulSoup

bew = []
w = []
#fileter urls 
def url1(bundle):
    ex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(ex,bundle)
    return [x[0] for x in url]

def spli(bew,lol):
    for link in lol.find_all('a'):
        bew.append(link.get('href'))
    return bew

def withouthttp(bew):
    return 0

if __name__ == '__main__':
    boom = requests.get("https://stackoverflow.com/questions/1918270/python-lists-append-return-value").text
    #print(url1(boom))
    soup = BeautifulSoup(boom, 'html.parser')
    spli(bew,soup)
    print(bew)    