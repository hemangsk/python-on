from bs4 import BeautifulSoup
import urllib2
import wget


print "Welcome to mathforcollege.com Numerical Method Chapters Downloader \n"




#The million dollar base url
url="http://nm.mathforcollege.com/topics/index.html"


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

def find_pdf_links(y):

        for plink in y:
            if ('.pdf' in plink and 'http://mathforcollege.com/nm/' in plink and 'ppt' not in plink and 'problem' not in plink and 'quiz' not in plink and 'example' not in plink):
                #collect_links.append(plink)
                filename=wget.download(plink)

def make_things_alright(y):
        #iterators
        i=0
        for text in y:
            if 'http:' not in text and 'https:' not in text and 'mailto' not in text:
                filter_stuff.append(text)
                filter_stuff[i]='http://nm.mathforcollege.com/topics/'+text
                i=i+1
        return filter_stuff

all_links= get_all_links(get_page(url))
chapters = make_things_alright(all_links) #filtering links


#iterators
i=0

for text in chapters:
        i=i+1
        print "Downloading Chapter "+ i
        find_pdf_links(get_all_links(get_page(text)))

print "Download Complete!"
