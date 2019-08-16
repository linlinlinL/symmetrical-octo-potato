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
# time.sleep(1)
head['User-Agent']='User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

#for ti in range(1):
'''time.sleep(3)
nextPage = drv.find_element_by_xpath("//a[@href='publicApplyServlet?command=findPublicApplyList&orgCode=&pager.offset=10']")
nextPage.click()'''
address='http://221.232.152.210/PBBS/publicnoticeservlet?command=findAllPublicNoticeList&flag=hppfBulletinList&pager.offset=1500'
x=1500
for w in range(239):
    # time.sleep(3)
    drv.get(address)
    # time.sleep(5)
    elements = drv.page_source
    time.sleep(1)
    soup = BeautifulSoup(elements, 'html.parser')
    time.sleep(1)
    file = open('项目环评受理情况', 'w', encoding='utf-8')
    target_url = address
    time.sleep(1)

    for li in soup.body.find_all('a',class_='hh14'):

        if (li.get('href') == None):
            time.sleep(1)
        else:
            title = str(li)
            a = title.find('">')
            title = title[a + 2:-4]
            title=title.replace('/',"")
            title=title.replace('?',"")
            title=title.replace('\t',"")
            title=title.replace('*',"")
            title=title.strip()
            print(title)

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

            for lin in soup.find_all('a',value='下载附件'):
                txt = str(lin.get('onclick'))
                #time.sleep(1)

                if (txt[:10] == 'downloadSN'):
                    time.sleep(1)
                    x1=txt[12:44]
                    x2=txt[47:51]
                    x3=txt[53:55]
                    print(x1)
                    print(x2)
                    print(x3)
                    href ='http://221.232.152.210/PBBS/publicnoticeservlet?command=downloadFile&instanceuuid='+x1+'&itemUuid='+x2+'&SN='+x3
                    print(href)
                    resource = requests.get(href)
                    time.sleep(1)

                    with open(str(title)+'.pdf', mode='wb') as fh:
                        fh.write(resource.content)
                        time.sleep(5)

                elif(txt[:8] == 'download'):
                    x1 = txt[10:42]
                    href='http://221.232.152.210/PBBS/publicnoticeservlet?command=downloadReplyFile&instanceuuid='+x1
                    resource = requests.get(href)
                    time.sleep(1)

                    with open(str(title) + '.doc', mode='wb') as fh:
                        fh.write(resource.content)
                        time.sleep(5)
                    break
                else:
                    continue
            time.sleep(2)
    x = x+10
    address = str(address)
    address = 'http://221.232.152.210/PBBS/publicnoticeservlet?command=findAllPublicNoticeList&flag=hppfBulletinList&pager.offset='+str(x)
    print(address)
    time.sleep(5)