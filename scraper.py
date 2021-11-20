import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
import mimetypes

merged_urls=set() #x=[]
internal_links=set()
external_links=set()
subdomains=set()
cookies=dict()
hipper=set()

with open('domains.txt') as f:
    for i in f:
        subdomains.add(i.strip('\n'))
with open('cookie.json') as c: 
    for i in json.loads(c.read()):
        cookies.update(i)
        break
def extern(*types):
    for ext in mimetypes.types_map:
        print(ext)
        if mimetypes.types_map[ext].split('/')[0] == types:
            yield ext


def url1(bundle):
    ex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(ex,bundle)
    k =[k[0] for k in url] 
    merged_urls.update(set(k))
    return merged_urls

def spli(lol):
    for link in lol.find_all('a'):
        hipper.add(link.get('href'))

def merge(lol):
    for link in lol.find_all('base'):
        baseurl=link.get('href')
        if baseurl:
            for i in hipper:
                if str(i).startswith("/"):
                    merged_urls.add(baseurl+i)

    else:
        for i in hipper.copy():
            if str(i).startswith("/"):
                merged_urls.add(f"https://{domain}"+i)
            

def loops(logs=merged_urls):
    for i in subdomains:
        for x in logs:
            #print(urlparse(x).netloc)
            if urlparse(x).netloc == str(i.strip()):
                internal_links.add(x)
                r = requests.get(x,cookies).text
                b = BeautifulSoup(r, 'html.parser')
                url1(r)
                spli(b)
                merge(b)
                print(x)
            elif urlparse(x).netloc != str(i.strip()):
                external_links.add(x)
    return loops()
#    while internal_links:
                
if __name__ == '__main__':
    domain="hackerone.com"
    boom = requests.get(f"https://{domain}/").text
    soup = BeautifulSoup(boom, 'html.parser')
    spli(soup)
    merge(soup)
    url1(boom)
    loops()
    print(internal_links)
    
