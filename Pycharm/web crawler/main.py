import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page=1
    while(page<=max_pages):
        url='http://fetchbusiness.com/show/Web%20Marketing/&page_cg='+str(page)+'&#.WGsauVMrJEY'
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'target':'_blank'}):
            href=link.get('href')
            print('href')
        page+=1


trade_spider(1)
