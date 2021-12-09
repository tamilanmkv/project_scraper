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
    user_agent = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:94.0)"}
    return requests.get(x,cookies,headers=user_agent,timeout=2).text     
def bef(r):
    url1(r)
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
                    with open('imagesFiles.txt','a') as f:
                        print(x.strip(), file=f)
                elif ex_path.endswith(".js") or ex_path.endswith("js.map"):
                    with open('javascriptFiles.txt','a') as f:
                        print(x.strip(), file=f)
    cop =set()
    with ThreadPoolExecutor(max_workers=3) as executor:
        for x in logs:
            if str(urlparse(x).netloc) in subdomains and str(x) not in thavaiillatha_onions and x not in internal_links: 
                cop.add(executor.submit(colec, x))
                internal_links.add(x)
                with open(f"{domain}_internal_links.txt","a") as f:
                    print(x.strip(), file=f)
                     
            else:
                external_links.add(x)
                with open(f"{domain}_external_links.txt","a") as f:
                    print(x.strip(), file=f)
        for r in as_completed(cop):
            r = r.result()
            executor.map(bef(r))
    return logs

#condition the link
def scrap(max_count=5):
    global total_urls_visited
    total_urls_visited += 1
    while max_count > 0:
        max_count -=1
        loops(merged_urls)
               
if __name__ == '__main__':
#    domain = "hackerone.com"
    import os
    import argparse
    parser = argparse.ArgumentParser(description="Link Scraper Tool with Python")
    parser.add_argument('domain', help="The main domain name .")
    parser.add_argument("-m",'--max_count',help="Max number of page want to scrap", default=10, type=int)  
    parser.add_argument('-l','--links',help="old scraped links dont scrap again same word",required=False) 
    parser.add_argument('-s',"--sub",help="subdomains of your domains",required=True)
    parser.add_argument('-c',"--cookie",help="use cookie editor to export the cookie save *.json format",required=False,default=0) 
    args= parser.parse_args()
    domain  = args.domain
    files = str(args.links)   
    if len(files) > 0:
        if os.path.isfile(files):
            with open(files) as f:
                for fil in f:
                    internal_links.add(fil)
    
    sub = str(args.sub)
    if len(sub) > 0:
        with open(sub) as f:
            for i in f:
                subdomains.add(i.strip('\n'))
    if args.cookie:
        with open(args.cookie) as c: 
            for i in json.loads(c.read()):
                cookies.update(i)
                break

    max_count = args.max_count
    de = colec(f"https://{domain}/")
    bef(de)
    scrap()
    print(internal_links)

