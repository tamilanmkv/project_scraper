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
        yield hipper.add(link.get('href'))
        

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
            
#loop the process 
thavaiillatha_onions=set()
def loops():
    logs = merged_urls.copy()
    if len(internal_links) > 0:
        for k in internal_links:
            if k in logs:
               return logs.remove(k) 
    for i in subdomains:
        for x in logs:    
            if urlparse(x).netloc == i:
                for j in extern('image'):
                    ex_path= urlparse(x).path
                    if ex_path.endswith(j) and ex_path.endswith('.pdf'):
                        thavaiillatha_onions.add(x)
                else:
                    r = requests.get(x,cookies).text
                    b = BeautifulSoup(r, 'html.parser')
                    url1(r)
                    spli(b)
                    merge(b) 
                    print(x)
                    internal_links.add(x) 
            elif urlparse(x).netloc != str(i.strip()):
                external_links.add(x)
    return loops()
#    while internal_links:

#condition the link
def scrap(max_count=1000):
    global total_urls_visited
    total_urls_visited += 1
    loops()
    for i in range(len(internal_links)):
        if total_urls_visited > max_count:
            break 
               
if __name__ == '__main__':
    domain="hackerone.com"
    boom = requests.get(f"https://{domain}/").text
    soup = BeautifulSoup(boom, 'html.parser')
    spli(soup)
    merge(soup)
    url1(boom)
    scrap()    
    print(internal_links)