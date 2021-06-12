from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote
import re

cala_biblia = ''

for i in range(1,1111):

    print("rozdział %d" % i)

    pg = requests.get("http://biblia.deon.pl/rozdzial.php?id=%d" % i).text
    bs = BeautifulSoup(pg)
    tresc_div = bs.find("div", {'class': 'tresc'})

    for tag in tresc_div.find_all(True):
        tag.decompose()

    tresc = unquote(tresc_div.get_text())\
        .encode('utf-16').decode('iso8859_2').replace("\x00", "")\
        .replace("Ť","").replace("ţ","").replace("ť","").replace("˙","").replace("\n","").replace(r'\x20+',' ')

    cala_biblia += tresc

print(cala_biblia,  file=open('cala_biblia', 'w'))

