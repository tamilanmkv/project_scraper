import requests
import sys

from requests.api import request
from requests.sessions import session


url = 'https://hackerone.com/tamilan_mkv'
sess = requests.session()
sess.get(url)
