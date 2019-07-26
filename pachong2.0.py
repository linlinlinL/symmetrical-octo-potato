# coding:utf-8
from selenium import webdriver
from urllib import request
from bs4 import BeautifulSoup
import chardet
import requests
import time


drv=webdriver.Chrome('D:\webdriver\chromedriver')
drv.get('http://hbj.nanjing.gov.cn/njshjbhj/?id=278')
drv.switch_to.frame('DataList')
elements=drv.page_source
soup = BeautifulSoup(elements, 'html.parser')

file=open('项目环评受理情况','w',encoding='utf-8')
target_url='http://hbj.nanjing.gov.cn/njshjbhj/?id=278'
head={}
head['User-Agent']='User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

for li in soup.body.find_all('a'):
    if (li.get('href')==None):
        time.sleep(1)
    else:
        link = li.get('href')
        response = request.urlopen(link)
        html = response.read()
        charset = chardet.detect(html)
        tp = charset['encoding']
        html = html.decode(tp)
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find()
        for lin in soup.find_all('a'):
            txt = str(lin.get('href'))
            if (txt[-4:] == '.pdf'):
                p = str(lin.get('href'))
                b = link[0:41]
                address = str(b) + p[1:]
                print(li.get('title'),address)
                resource = requests.get(address)
                title=p[-21:-13]
                with open(str(title)+'.pdf', mode='wb') as fh:
                    fh.write(resource.content)
            else:
                continue
        time.sleep(2)
