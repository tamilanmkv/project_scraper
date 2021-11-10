#!/bin/env python3

import re
import requests
from bs4 import BeautifulSoup
import numpy as np

split_urls = list() #bew = [] #spli functions output #spli functions output
regex_urls = list() #w = [] #url1 functions output
merged_urls=list() #x=[]
nohttps=list() #


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
    dubs = np.hstack(bew+w)
    f =list(set(dubs))
    return x.append(f)

#filter the hipper link and merage the domain url 
def merge(x,nohttps,domain):
    for i in np.hstack(x):
        if str(i).startswith("/"):
            nohttps.append(f"https://{domain}"+i)             

if __name__ == '__main__':
    domain="stackoverflow.com"
    boom = requests.get(f"https://{domain}/").text
    soup = BeautifulSoup(boom, 'html.parser')
    spli(split_urls,soup)
    url1(boom,regex_urls)
    removedub(split_urls,merged_urls,regex_urls)
    merge(merged_urls,nohttps,domain)
    print(nohttps)
       #litle