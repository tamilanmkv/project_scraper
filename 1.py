import mimetypes
from urllib.parse import urlparse

def get_extensions_for_type(general_type):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type: 
            yield ext

#VIDEO = tuple(get_extensions_for_type('video'))
#AUDIO = tuple(get_extensions_for_type('audio'))
#IMAGE = tuple(get_extensions_for_type('image'))

#print("VIDEO = " + str(VIDEO))
#print('')
#print("AUDIO = " + str(AUDIO))
#print('')
#print("IMAGE = " + str(IMAGE))
m=set(get_extensions_for_type('image'))
link = {'https://google.com/image.jpg','https://hackerone.cm/','https://hackerone.com/gogo.png'}

for i in m:
    for x in link:
        k = urlparse(x).path
        if k.endswith(i):
            print(x)
