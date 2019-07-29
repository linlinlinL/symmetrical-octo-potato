# coding:utf-8
from selenium import webdriver
from urllib import request
from bs4 import BeautifulSoup
import chardet
import requests
import time

drv=webdriver.Ie('D:\webdriver\IEDriverServer')
drv.get('http://hbj.wuhan.gov.cn/hpgs.jspx?type=1')
time.sleep(5)
head={}
time.sleep(1)
head['User-Agent']='User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
datalist=drv.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/ul/li/iframe")
drv.switch_to.frame(datalist)
'''for ti in range(12):
    time.sleep(3)
    nextPage = drv.find_element_by_xpath("//a[@id='next']")
    nextPage.click()'''

for w in range(239):
    elements = drv.page_source
    time.sleep(1)
    soup = BeautifulSoup(elements, 'html.parser')
    time.sleep(1)
    file = open('项目环评受理情况', 'w', encoding='utf-8')
    target_url = 'http://hbj.wuhan.gov.cn/hpgs.jspx?type=1'
    time.sleep(1)

    for li in soup.body.find_all('a',class_='hh14'):

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

            title=soup.find('td',class_='style2')
            title=str(title)
            a=title.find('>')
            title=title[a+2:-5]
            print(title)

            for lin in soup.find_all('a',value='下载附件'):
                txt = str(lin.get('onclick'))
                time.sleep(1)

                if (txt[:8] == 'download'):
                    time.sleep(1)
                    x1=txt[10:41]
                    x2=txt[45:48]
                    x3=txt[51:53]
                    print(x1)
                    print(x2)
                    print(x3)
                    href='http://221.232.152.210/PBBS/publicnoticeservlet?command=downloadFile&instanceuuid='+x1+'&itemUuid='+x2+'&SN='+x3

                    print(href)
                    resource = requests.get(href)
                    time.sleep(1)

                    with open(str(title)+'.pdf', mode='wb') as fh:
                        fh.write(resource.content)
                        time.sleep(5)

                else:
                    continue
            time.sleep(2)
    nextPage = drv.find_element_by_xpath("//a[@id='next']")
    nextPage.click()
    time.sleep(5)
