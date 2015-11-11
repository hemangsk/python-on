from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib
import urllib2
import wget
new_links=[]

browser = webdriver.Firefox()
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

def find_btech_links(links):
    for x in links:
        if "cse.php" in x:
            new_links.append("http://www.xampaperz.com/"+ x)
    return new_links
final_stuff=[]
def makeup(x,y):

    pos=x.find(".php")
    x=x[:pos-3]
    i=9
    stream="it"
    while(i<14):
        if i==9:
            string1="http://xampaperz.com/papers/img/btech/"+ stream + "/sem" + str(y[25]) + "/200"+str(i)+x+".jpg/"

            string2="http://xampaperz.com/papers/img/btech/"+ stream + "/sem" + str(y[25]) + "/200"+str(i)+x+"2.jpg/"

        else:
            string1="http://xampaperz.com/papers/img/btech/"+ stream + "/sem" + str(y[25]) + "/20"+str(i)+x+".jpg/"

            string2="http://xampaperz.com/papers/img/btech/"+ stream + "/sem" + str(y[25]) + "/20"+str(i)+x+"2.jpg/"
        final_stuff.append(string1)
        final_stuff.append(string2)
        i=i+1

url = 'http://www.xampaperz.com/'
browser.get(url)


page=browser.page_source

links=[]

f=open("adsa.txt","w")
f.write(page.encode("utf-8"))
f.close()
f=open("adsa.txt","r")
page=f.read()
f.close()
links=get_all_links(page)
new_links=find_btech_links(links)



for x in new_links:
    url=x

browser.get(url)


page=browser.page_source
links=[]

f=open("adsa.txt","w")
f.write(page.encode("utf-8"))
f.close()
f=open("adsa.txt","r")
page=f.read()
f.close()
startpoint=page.find("it1")

page=page[startpoint:]

links=get_all_links(page)

for x in links:
    if "1stsemcse" in x or "2ndsemcse" in x or "3rdsemcse" in x or "thsemcse" in x:
        new_links.append("http://www.xampaperz.com/"+ x)
qplinks=[]
new_links.pop(0)
cool=[]
for x in new_links:

    url=x
    browser.get(url)

    time.sleep(2)
    page=browser.page_source



    f=open("adsa.txt","w")
    f.write(page.encode("utf-8"))
    f.close()
    f=open("adsa.txt","r")
    page=f.read()
    f.close()
    startpoint=page.find("it1")
    endpoint=page.find("<script src=",startpoint)

    page=page[startpoint:endpoint]
    qplinks=get_all_links(page)

    for y in qplinks:
        d="http://xampaperz.com/"+y
        cool.append(d)


cooler=[]
for x in cool:

    url=x
    browser.get(url)

    time.sleep(2)
    page=browser.page_source



    f=open("adsa.txt","w")
    f.write(page.encode("utf-8"))
    f.close()
    f=open("adsa.txt","r")
    page=f.read()
    f.close()
    startpoint=page.find("it1")
    endpoint=page.find('</div>',startpoint)

    page=page[startpoint:endpoint]
    qplinks=get_all_links(page)
    for y in qplinks:
        d="http://xampaperz.com/"+y
        cooler.append(d)

print cooler

#g=open("finalstuff.txt","w")
#for x in final_stuff:
    #filename=wget.download(x)
    #g.write(x+"\n")
