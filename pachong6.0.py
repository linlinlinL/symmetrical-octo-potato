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
address='http://sthjj.cq.gov.cn/hjgl/hjyxpj/jsxmhpspqk/scjsxmhpxxgs/index_20.shtml'
xx=20
x=0
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

    for li in soup.body.find_all('a',target="_blank"):
        a=li.get('title')
        a=str(a)
        print(a[:2],a)
        if(a[:2]=='监测'):
            continue
        elif(a[:2]=='No'):
            continue
        else:
            x = x + 1
            if (x <7):
                continue
            else:
                title = li.get('title')
                title = title.replace('/', "")
                title = title.replace('?', "")
                title = title.replace(':', "")
                title = title.replace('"', "")
                title = title.replace('|', "")
                title = title.replace('<', "")
                title = title.replace('>', "")
                print(title)

                link = li.get('href')
                link='http://sthjj.cq.gov.cn'+str(link)
                time.sleep(1)
                print('link' + link)
                if (link[-4:] == '.pdf'):
                    txt1 = str(link)
                    resource = requests.get(txt1)
                    time.sleep(5)

                    with open(str(title) + '.pdf', mode='wb') as fh:
                        fh.write(resource.content)
                        time.sleep(5)
                elif (link[-5:] == '.docx'):
                    txt1 = str(link)
                    resource = requests.get(txt1)
                    time.sleep(5)

                    with open(str(title) + '.docx', mode='wb') as fh:
                        fh.write(resource.content)
                        time.sleep(5)
                elif (link[-4:] == '.doc'):
                    txt1 = str(link)
                    resource = requests.get(txt1)
                    time.sleep(5)

                    with open(str(title) + '.doc', mode='wb') as fh:
                        fh.write(resource.content)
                        time.sleep(5)
                elif (link[-4:] == '.xls'):
                    txt1 = str(link)
                    resource = requests.get(txt1)
                    time.sleep(5)

                    with open(str(title) + '.xls', mode='wb') as fh:
                        fh.write(resource.content)
                        time.sleep(5)
                elif (link[-4:]=='null'):
                    continue
                else:
                    re = requests.get(link)
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
                        right = str(lin.get('href'))
                        if (right[-4:] == '.pdf'):
                            txt1 = str(lin.get('href'))
                            resource = requests.get(txt1)
                            time.sleep(1)
                            title1 = lin.get('title')
                            title1 = li.get('title')
                            title1 = title1.replace('/', "")
                            title1 = title1.replace('?', "")
                            title1 = title1.replace(':', "")
                            title1 = title1.replace('"', "")
                            title1 = title1.replace('|', "")
                            title1 = title1.replace('<', "")
                            title1 = title1.replace('>', "")
                            print(title1)
                            time.sleep(5)

                            with open(str(title1) + '.pdf', mode='wb') as fh:
                                fh.write(resource.content)
                                time.sleep(5)
                        else:
                            continue



    xx = xx +1
    address = str(address)
    address = 'http://sthjj.cq.gov.cn/hjgl/hjyxpj/jsxmhpspqk/scjsxmhpxxgs/index_'+str(xx)+'.shtml'
    print(address)
    time.sleep(5)



