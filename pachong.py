import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
import lxml
from lxml import etree
#设置列表页URL的固定部分
url = 'https://beijing.anjuke.com/community//p'
#设置页面页的可变部分

#设置请求头部信息
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00146bd600000003582bfd1f'
}
m = 1
for i in range(60, 100):
    i = str(i)
    a = (url+i+'/')
    print(a)
    r = requests.get(url=a, headers=headers)
    time.sleep(5)

    html = r.content
    lj = BeautifulSoup(html, 'html.parser')
    for li in lj.find_all('a', target='_blank', style='max-width: 420px;'):
        href = str(li.get('href'))
        time.sleep(5)

        if m == 1:
            r1 = requests.get(url=href, headers=headers)
            ht1 = r1.content
            ht = ht1
            m = m+1
        else:
            r1 = requests.get(url=href, headers=headers)
            ht1 = r1.content
            ht = ht+ht1

#每次间隔1秒
time.sleep(1)
# 解析抓取的页面内容
lj = BeautifulSoup(ht, 'html.parser')
# 提取房源信息
houseTitle = lj.find_all('div', attrs={'class': 'comm-title'})
ti=[]
for b in houseTitle:
    house = b.get_text()
    house.replace(" ", "")
    house.replace("\n","")
    print(house)
    ti.append(house)

houseInfo = lj.find_all('dl', attrs={'class': 'basic-parms-mod'})
hi = []

for b in houseInfo:
    house = b.get_text()
    house.replace(" ", "")
    x = house.find('容')
    y = house.find('停车位')
    z = house.find('总户')
    h = house.find('开')
    print(house[z:y-1]+house[x:h])
    hi.append(house[z:y-1]+house[x:h])
    # for item in hi:
    #     print(item)
house = pd.DataFrame({'title': ti, 'houseinfo': hi})
house.to_excel("test.xls")
print(house.head())




