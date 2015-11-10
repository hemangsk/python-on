import urllib2
from bs4 import BeautifulSoup

f=open("ds.txt","r")
g=open("read.txt","w")
soup=BeautifulSoup(f.read())
text=soup.get_text()
g.write(text.encode("utf-8"))
