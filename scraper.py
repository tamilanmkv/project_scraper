import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
import mimetypes
from concurrent.futures import ThreadPoolExecutor, as_completed

merged_urls=set() #x=[]
internal_links=set()
external_links=set()
subdomains=set()
cookies=dict()
hipper=set()
total_urls_visited=0


with open('domains.txt') as f:
    for i in f:
        subdomains.add(i.strip('\n'))
with open('cookie.json') as c: 
    for i in json.loads(c.read()):
        cookies.update(i)
        break

#all unknow extentions
def extern(types):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == types:
            yield ext

#regext the urls
def url1(bundle):
    ex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(ex,bundle)
    k =[k[0] for k in url] 
    merged_urls.update(set(k))
    return merged_urls

#hipper link collections
def spli(lol):
    for link in lol.find_all('a'):
        hipper.add(link.get('href'))
        

#if base tag is available or add the domain to hipper link
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
            
def colec(x):
    return requests.get(x,cookies).text
def bef(r):
    b=BeautifulSoup(r, 'html.parser')
    spli(b)
    merge(b)
    return b
#loop the process 
thavaiillatha_onions=set()
def loops(logs):
    logs = merged_urls.copy()
    if len(internal_links) > 0:
        for k in internal_links:
            if str(k) in logs:
                logs.remove(k)
    for x in logs:    
        k = urlparse(x).netloc
        if str(k) in subdomains:
            for j in extern('image'):
                ex_path= urlparse(x).path
                if ex_path.endswith(j) and ex_path.endswith('.pdf'):
                    thavaiillatha_onions.add(x)
    cop =set()
    with ThreadPoolExecutor(max_workers=10) as executor:
        for x in logs:
            if str(urlparse(x).netloc) in subdomains and str(x) not in thavaiillatha_onions:
                cop.add(executor.submit(colec, x))
                print(x)
    for r in as_completed(cop):
        url1(r.result())
        bef(r.result())
        #for x in logs:
         #   if str(urlparse(x).netloc) in subdomains and str(x) not in thavaiillatha_onions:
                #print(x)
          #      internal_links.add(x)
      #elif str(k) not in subdomains:
          #external_links.add(x)
    return logs

#condition the link
def scrap(max_count=1000):
    global total_urls_visited
    total_urls_visited += 1
    while max_count > 0:
        loops(merged_urls)
        max_count -=1

if __name__ == '__main__':
    domain="hackerone.com"
    req = colec(f"https://{domain}/")
    bef(req)
    print(merged_urls)
    scrap()    

