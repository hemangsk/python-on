from bs4 import BeautifulSoup
import urllib2
import wget
import dryscrape


print "Welcome to Xampaperz Downloader \n"




#The million dollar base url
url="http://xampaperz.com/cse.php"


#Variables
filter_stuff=[] #used in function make_things_alright as a temporary array which stores useful links
chapters=[] #This array will store all the useful links from webpage discarding other links
pdf_links=[]

def get_page(url):
    f = urllib2.urlopen(url)
    page = f.read()
    f.close()
    return page

def get_next_target(page):
        start_link = page.find('<a href="')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

def get_all_links(page):
        links = []
        while True:
            url,endpos = get_next_target(page)
            if url:
                links.append(url)
                page = page[endpos:]
            else:
                break
        return links

def find_viewjpg_links(y):

        for plink in y:


                filename=wget.download(plink)



all_links= get_all_links(get_page(url))
new_links=[]
new_links2=[]

for x in all_links:

    if "1stsem" in x or "2ndsem" in x or "3rdsem" in x or "thsem" in x:
        x="http://xampaperz.com/"+x
        new_links.append(x)
        session = dryscrape.Session()
        session.visit(x)
        response = session.body()
        print response
        soup = BeautifulSoup(response)
        print soup.get_text()
