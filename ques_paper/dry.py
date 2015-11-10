from selenium import webdriver
from bs4 import BeautifulSoup
import time


browser = webdriver.Firefox()

url = 'http://www.xampaperz.com/1stsemcse.php'
browser.get(url)
time.sleep(10)

page=browser.page_source
f=open("adsa.txt","w")
f.write(page.encode("utf-8"))
f.close()
