import urllib2
from bs4 import BeautifulSoup


print "Welcome ! \n"




#The million dollar base url
url="http://www.geeksforgeeks.org/data-structures"


#Variables
filter_stuff=[] #used in function make_things_alright as a temporary array which stores useful links
chapters=[] #This array will store all the useful links from webpage discarding other links
pdf_links=[]

def get_page(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Chrome/5.0')]
    response = opener.open(url)
    page = response.read()
    return page

def get_next_target(page):
        start_link = page.find('<a href="')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote
new_links=[]
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
fresh_links=[]
links =get_all_links(get_page(url))
for x in links:
    if "category" not in x and "/data-structures" not in x and "fundamentals-of-algorithms" not in x and "facebook" not in x:
        fresh_links.append(x)


i=0
j=0
for x in fresh_links:
    i=i+1
    j=j+1
    if i>25 and j<(len(fresh_links)-31):
        new_links.append(x)
print len(new_links)
f=open("G.txt","w")
for x in new_links:
    page=get_page(x)
    startpoint=page.find('<h1 class="entry-title">')
    print startpoint

    endpoint =page.find('<script async src')
    soup=BeautifulSoup(page[startpoint:endpoint])
    text=soup.get_text()
    f.write(text.encode("utf-8"))



#for x in fresh_links:

#    soup = BeautifulSoup(urllib2.urlopen(x).read())
#    text=soup.get_text()
