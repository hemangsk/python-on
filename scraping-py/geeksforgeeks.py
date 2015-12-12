from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import sys
Soup=BeautifulSoup
links=[]
url="http://www.geeksforgeeks.org/data-structures/"
f=urllib2.urlopen(url)
page=f.read()
f.close()
page=unicode(page,'utf-8')
soup=Soup(page)
j=0
for a in soup.findAll('a', href=True):
    if "http://geeksquiz.com/linked-list-set-1-introduction/" in a['href']:
        j=1
    if j==1:
        links.append(a['href'])
i=0
for x in links:
    if "#" in x:
        links.pop(i)
    i=i+1
print links
final=open("final.txt","w")
for x in links:
    print x
    f=urllib.urlopen(x)
    page=f.read()
    f.close()
    page=unicode(page,'utf-8')
    page=page[page.find("<header class="):page.find("<script async src=")]
    soup=Soup(page)
    final.write(soup.getText().encode('utf-8'))
