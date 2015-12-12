from BeautifulSoup import BeautifulSoup
import urllib2
import wget
import requests
Soup=BeautifulSoup
import BeautifulSoup

str1="Covering the nitty-gritties of C++ templates"
str2="This article, along with any associated source code and files, is licensed under"
url="http://www.codeproject.com/Articles/257589/An-Idiots-Guide-to-Cplusplus-Templates-Part";
f=urllib2.urlopen(url)
page=f.read()
f.close()

page=page[page.find(str1):page.find(str2)]

soup=Soup(page)
text = soup.getText()
f=open("Templates.txt", "w")
f.write(text.encode("utf-8"))
f.close()
