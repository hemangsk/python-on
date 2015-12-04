from BeautifulSoup import BeautifulSoup
import urllib2
import wget
import requests
Soup=BeautifulSoup
import BeautifulSoup
url="http://xampaperz.com/xampaperz/xampaperz/MAIT/xampaperz/subject.php?id=1&semkey=8&sem=8thsemcse&semester=8th&main=xampaerl_cse&stream_get=Computer"+ "%20"+"Science"
f=urllib2.urlopen(url)
page=f.read()
f.close()

soup=Soup(page)
links=[]
for a in soup.findAll('a', href=True):
    if "subject" in a['href']:
        links.append(a['href'])

fresh=[]

for a in links:
    a="http://xampaperz.com/xampaperz/xampaperz/MAIT/xampaperz/" +a

    a = a[: a.find("Computer ")] + "Computer" + "%20" +"Science/"

    fresh.append(a)

paper=[]
for a in fresh:
    f=urllib2.urlopen(a)
    page=f.read()
    f.close()
    soup=Soup(page)
    for a in soup.findAll('a', href=True):
        if "paper-viewer" in a['href']:
            paper.append("http:xampaperz/xampaperz/MAIT/xampaperz/" + a['href'])
final=[]
for a in paper:
    a= a[a.find("&paper_url")+len("&paper_url")+1:a.find(".jpg")] +".jpg"
    print a
    final.append(a)

i=0
for x in final:
    response = requests.get(x)
    if response.status_code == 200:
        f = open("8th Sem final" + str(i)+ ".jpg", 'wb')
        f.write(response.content)
        f.close()
    i=i+1
