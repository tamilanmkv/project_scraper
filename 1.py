import mimetypes

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
m=get_extensions_for_type('image')
link = {'https://google.com/image.jpg','https://hackerone.cm/','https://hackerone.com/gogo.png'}
k = set()
for i in get_extensions_for_type('image'):
    k.add(i)

print(k)
def m():
    for i in k.copy():
        print(i)
        k.remove(i) 
    return m() 
for i in range(100):
    k.add(i)
    m()

print("\n\n\n\n\n\n\n",k)
