#!/bin/env python3

import re
import requests
from bs4 import BeautifulSoup

bew = []
w = []
x=[]
nohttps=[]
#fileter urls with regex
def url1(bundle,x):
    ex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(ex,bundle)
    k =[k[0] for k in url] 
    return x.append(k)

#filter url in `a` href tags
def spli(bew,lol):
    for link in lol.find_all('a'):
        bew.append(link.get('href'))
    return bew

#map data structure to remove dublicates from array
def removedub(bew,w,x):
    dubs = bew+x
    f = list(set(dubs))
    return w

#filter the hipper link and merage the domain url 
def merge(a):
    for i in a:
        for a
            if i.startswith("/"):
                a.append('https://hello.com'+i)
                return a.remove(i)

if __name__ == '__main__':
    boom = requests.get("https://stackoverflow.com/questions/1918270/python-lists-append-return-value").text
    #print(url1(boom))
    soup = BeautifulSoup(boom, 'html.parser')
    spli(x,soup)
   # print(bew) 
    url1(boom,w)
    removedub(bew,w,x)
    print(merge(w))
    #lol