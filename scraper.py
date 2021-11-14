import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
from requests.api import request
from requests.sessions import session

merged_urls=set() #x=[]
internal_links=set()
external_links=set()
subdomains=set()
cookies=dict()

with open('/tmp/domains.txt') as f:
    for i in f:
        subdomains.add(i.strip('\n'))
with open('/tmp/cookie.json') as c: 
    for i in json.loads(c.read()):
        cookies.update(i)
        break

def url1(bundle):
    ex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(ex,bundle)
    k =[k[0] for k in url] 
    merged_urls.update(set(k))
    return merged_urls

def spli(lol):
    for link in lol.find_all('a'):
        merged_urls.add(link.get('href'))
    return merge(lol)

def merge(lol):
    for link in lol.find_all('base'):
        baseurl=link.get('href')
        if baseurl:
            for i in merged_urls:
                if str(i).startswith("/"):
                    merged_urls.add(baseurl+i)
                    return merged_urls
    else:
        for i in merged_urls:
            if str(i).startswith("/"):
                merged_urls.add(f"https://{domain}"+i)
                return merged_urls

def loops():

    for i in subdomains:
        for x in merged_urls.copy():
            if urlparse(x).netloc == str(i):
                internal_links.add(x)
                continue
    for k in internal_links:
        r = requests.get(k,cookies).text
        b = BeautifulSoup(r, 'html.parser')
        url1(r)
        print(spli(b))
        print(merged_urls)       
#        b = BeautifulSoup(r, 'html.parser')
       # print(url1(r))
       # print("\n\n\n\n\n")
       # print(spli(b))
#                   '''  req = requests.get(x).text
#                        url1(req)
#                        soup = BeautifulSoup(req,'html.parser')
#                        spli(temp,soup)
#                    for k in temp:
#                        if str(k).startswith('/'):
#                            temp.add(f'https://{domain}'+k)
#                            return k'''
    


if __name__ == '__main__':
    domain="hackerone.com"
    boom = requests.get(f"https://{domain}/").text
    soup = BeautifulSoup(boom, 'html.parser')
    spli(soup)
    url1(boom)
    loops()
    