#!/bin/env python3

import re
import requests
from bs4 import BeautifulSoup
import numpy as np
from urllib.parse import urlparse

split_urls = list() #bew = [] #spli functions output #spli functions output
regex_urls = list() #w = [] #url1 functions output
merged_urls=list() #x=[]
internal_links=set()
external_links=set()

#fileter urls with regex
def url1(bundle,regex_urls):
    ex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(ex,bundle)
    k =[k[0] for k in url] 
    return regex_urls.append(k)

#filter url in `a` href tags
def spli(split_urls,lol):
    for link in lol.find_all('a'):
        split_urls.append(link.get('href'))
    return split_urls

#map data structure to remove dublicates from array
def removedub(split_urls,merged_urls,regex_urls):
    dubs = np.hstack(split_urls+regex_urls)
    f =list(set(dubs))
    return merged_urls.append(f)

#filter the hipper link and merage the domain url 
def merge(merged_urls,domain,lol):
    for link in lol.find_all('base'):
        baseurl=link.get('href')
        if baseurl.count('base') > 0:
            for i in np.hstack(merged_urls):
                if str(i).startswith("/"):
                    merged_urls.add(baseurl+i)
    else:
        for i in np.hstack(merged_urls):
            if str(i).startswith("/"):
                merged_urls.add(f"https://{domain}"+i)
    
#only matched domain loops and subdomains multi links
def loops(inp,oup):
    with open('/tmp/domins.txt') as f:
    for i in f:
        
        

if __name__ == '__main__':
    domain="hackerone.com"
    boom = requests.get(f"https://{domain}/").text
    soup = BeautifulSoup(boom, 'html.parser')
    spli(split_urls,soup)
    url1(boom,regex_urls)
    removedub(split_urls,merged_urls,regex_urls)
    merge(merged_urls,domain,soup) 
    loops(merged_urls,internal_links)
       #litle