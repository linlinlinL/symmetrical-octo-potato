# coding:utf-8
from selenium import webdriver
from urllib import request
from bs4 import BeautifulSoup
import chardet
import requests
import os  #导入os模块
import win32
import time
import docx

drv=webdriver.Ie('D:\webdriver\IEDriverServer')
time.sleep(5)
head={}
time.sleep(1)
head['User-Agent']='User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

#for ti in range(1):
'''time.sleep(3)
nextPage = drv.find_element_by_xpath("//a[@href='publicApplyServlet?command=findPublicApplyList&orgCode=&pager.offset=30']")
nextPage.click()'''
address='http://www.nanjing.gov.cn/zdgk//214/275/index_12333.html'
x=1
for w in range(239):
   # time.sleep(3)
    drv.get(address)
    # time.sleep(5)
    elements = drv.page_source
    time.sleep(1)
    soup = BeautifulSoup(elements, 'html.parser')
    time.sleep(1)
    # file = open('项目环评受理情况', 'w', encoding='utf-8')
    target_url = address
    time.sleep(1)
    print(soup.body.find_all('a',class_='titleshow'))

    for li in soup.body.find_all('a',class_='titleshow'):
        print(li)
        x = x + 1
        if (x<470):
            print(x)
            time.sleep(1)

            continue
        else:
            print(x)
            title = str(li)
            a = title.find('">')
            title = title[a + 2:-4]
            title=title.replace('/',"")
            title=title.replace('?',"")
            title=title.replace('*',"")
            title=title.replace('\t',"")
            title=title.strip()
            print(title)

            link = li.get('href')
            time.sleep(1)

            re=requests.get(link)
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

            with open(str(title) + '.html', mode='wb') as fh:
                fh.write(re.content)
                time.sleep(5)

            for lin in soup.find_all('a'):
                right=str(lin.get('href'))
                if (right[:2]=='./'):
                    txt1 = str(lin.get('href'))
                    txt=str(link[:38])+txt1[2:]
                    print(txt)
                    time.sleep(1)
                    resource = requests.get(txt)
                    time.sleep(1)

                    title1 = str(lin)
                    a = title1.find('">')
                    title1 = title1[a + 2:-4]
                    print(title1)
                    time.sleep(5)

                    with open(str(title1) + '.pdf', mode='wb') as fh:
                        fh.write(resource.content)
                        time.sleep(5)
                else:
                    time.sleep(5)
                    continue


