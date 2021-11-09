#!/bin/env python3

import re
import requests
from bs4 import BeautifulSoup

bew = []
w = []
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

##add the hipper links into join the domain name
def withouthttp(soup):
    #print(url1(soup))
    return 0

#map data structure to remove dublicates from array
def removedub(bew,w):
    def Convert(a):
        it = iter(a)
        res_dct = dict(zip(it, it))
        return res_dct
    dubs = bew+w
    dubs = list(dict.fromkeys(Convert(dubs)))
    return dubs

#filter the hipper link and merage the domain url 
def merge():
    

if __name__ == '__main__':
    boom = requests.get("https://stackoverflow.com/questions/1918270/python-lists-append-return-value").text
    #print(url1(boom))
    soup = BeautifulSoup(boom, 'html.parser')
    spli(bew,soup)
   # print(bew) 
    url1(boom,w)
    print(removedub(bew,w))


    #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