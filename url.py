#!/bin/env python3

import re
import requests
from bs4 import BeautifulSoup

bew = [] #spli functions output
w = [] #url1 functions output
x=[]
nohttps=[]
#fileter urls with regex
def url1(bundle,w):
    ex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(ex,bundle)
    k =[k[0] for k in url] 
    return w.append(k)

#filter url in `a` href tags
def spli(bew,lol):
    for link in lol.find_all('a'):
        bew.append(link.get('href'))
    return bew

#map data structure to remove dublicates from array
def removedub(bew,x,w):
    dubs = bew+w
    print(dubs)
    f = [list(set(k)) for k in dubs]
    return x.append(f)

#filter the hipper link and merage the domain url 
def merge(x,nohttps,domain):
    for i in a:
        if str(i).startswith("/"):
            nohttps.append(f"https://{domain}"+i)             

if __name__ == '__main__':
    domain="stackoverflow.com"
    boom = requests.get(f"https://{domain}/").text
    #print(url1(boom))
    soup = BeautifulSoup(boom, 'html.parser')
    spli(bew,soup)
   # print(bew) 
    url1(boom,w)
    removedub(bew,x,w)
    merge(bew,nohttps,domain)
    print(x)
    
       #lol