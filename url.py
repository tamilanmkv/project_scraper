#!/bin/env python3

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen

#split_urls = set() #bew = [] #spli functions output #spli functions output
#regex_urls = set() #w = [] #url1 functions output
merged_urls=set() #x=[]
internal_links=set()
external_links=set()

#fileter urls with regex
def url1(bundle,merged_urls):
    ex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(ex,bundle)
    k =[k[0] for k in url] 
    return merged_urls.update(set(k))

#filter url in `a` href tags
def spli(merged_urls,lol):
    for link in lol.find_all('a'):
        merged_urls.add(link.get('href'))
    return merged_urls


#filter the hipper link and merage the domain url 
def merge(merged_urls,domain,lol):
    for link in lol.find_all('base'):
        baseurl=link.get('href')
        if baseurl.count('base') == 1:
            for i in merged_urls:
                if str(i).startswith("/"):
                    merged_urls.add(baseurl+i)
    else:
        for i in merged_urls:
            if str(i).startswith("/"):
                return merged_urls.add(f"https://{domain}"+i)
                
    
#only matched domain loops and subdomains multi links
def loops(inp,oup,domain):
    temp= set(inp)
    subdomains= set()
    with open('/tmp/domains.txt') as f:
        for i in f:
            print(i)
            subdomains.add(i.strip('\n'))      
    
    for x in temp:
        if urlparse(x).netloc == i:
            if str(x).startswith('https'):
                req = requests.get(x).text
                url1(req,inp)
                soup = BeautifulSoup(req,'html.parser')
                spli(inp,soup)
            for k in temp:
                if str(k).startswith('/'):
                    temp.add(f'https://{domain}'+k)
                    return k
    oup.update(temp)
                    
if __name__ == '__main__':
    domain="hackerone.com"
    boom = requests.get(f"https://{domain}/").text
    soup = BeautifulSoup(boom, 'html.parser')
    spli(merged_urls,soup)
    url1(boom,merged_urls)
    merge(merged_urls,domain,soup) 
    loops(merged_urls,internal_links,domain)
    print(merged_urls)
    