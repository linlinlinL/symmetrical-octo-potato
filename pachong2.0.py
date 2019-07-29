# coding:utf-8
from selenium import webdriver
from urllib import request
from bs4 import BeautifulSoup
import chardet
import requests
import time

x=1
drv=webdriver.Chrome('D:\webdriver\chromedriver')
drv.get('http://hbj.nanjing.gov.cn/njshjbhj/?id=278')
time.sleep(5)
head={}
time.sleep(1)
head['User-Agent']='User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
drv.switch_to.frame('DataList')
for ti in range(12):
    time.sleep(3)
    nextPage = drv.find_element_by_xpath("//a[@id='next']")
    nextPage.click()

for w in range(10):
    elements = drv.page_source
    time.sleep(1)
    soup = BeautifulSoup(elements, 'html.parser')
    time.sleep(1)
    file = open('项目环评受理情况', 'w', encoding='utf-8')
    target_url = 'http://hbj.nanjing.gov.cn/njshjbhj/?id=278'
    time.sleep(1)

    for li in soup.body.find_all('a'):

        if (li.get('href') == None):
            time.sleep(1)
        else:
            link = li.get('href')
            time.sleep(1)

            response = request.urlopen(link)
            html = response.read()
            time.sleep(1)
            charset = chardet.detect(html)
            tp = charset['encoding']
            time.sleep(1)
            html = html.decode(tp)
            time.sleep(5)

            soup = BeautifulSoup(html, 'html.parser')
            a = soup.find()
            time.sleep(1)

            for lin in soup.find_all('a'):
                txt = str(lin.get('href'))
                time.sleep(1)

                if (txt[-4:] == '.pdf'):
                    time.sleep(1)

                    p = str(lin.get('href'))
                    b = link[0:41]
                    time.sleep(1)
                    address = str(b) + p[1:]
                    time.sleep(1)
                    print(address)
                    time.sleep(1)
                    resource = requests.get(address)
                    title = li.get('title')
                    time.sleep(1)

                    with open(str(x)+' '+str(title[-11:-1]) + '.pdf', mode='wb') as fh:
                        fh.write(resource.content)
                        x=x+1
                        time.sleep(5)

                else:
                    continue
            time.sleep(2)
    nextPage = drv.find_element_by_xpath("//a[@id='next']")
    nextPage.click()
    time.sleep(5)
