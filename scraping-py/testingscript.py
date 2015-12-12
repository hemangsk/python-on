import wget
import urllib2
from BeautifulSoup import BeautifulSoup
Soup=BeautifulSoup
import BeautifulSoup
i=0
url="http://stim.ee.uh.edu/education/ece-3340-numerical-methods/"
f=urllib2.urlopen(url)
page=f.read()
f.close()
soup=Soup(page)
for link in soup.findAll('a', href=True):
    if "bitbucket" in link['href'] and "ppt" not in link['href']:
        filename=wget.download(link['href'])
