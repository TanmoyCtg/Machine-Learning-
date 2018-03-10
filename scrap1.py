from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import csv
from datetime import datetime
page_link = ["https://www.kdnuggets.com/2018/03/tutorials.html"]

data = []
for pg in page_link:
    page = urlopen(pg)
# print (page)
soup = BS(page,"html5lib")
# print (soup)
for ultag in soup.find_all('ul',attrs={'class':'three_ul test'}):
    for litag in ultag.find_all('li'):
        for atag in litag.find_all('a'):
            href = atag.get('href')
            print (href)
            with open('kdnuggets.csv','a') as csv_file:
                writer = csv.writer(csv_file)
                data.append(href)
                for href in data:
                    writer.writerow([href])


            
