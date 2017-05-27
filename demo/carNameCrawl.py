#coding=utf-8
'''
Created on 2016.10.30

@author: ZakeXu

@汽车之家：http://car.autohome.com.cn/zhaoche/pinpai/#pvareaid=103405
'''
import urllib2
from lxml import etree

def carNameCrawl():
    path = "../data/car_name"
    fid = open(path, 'w')
    
    url = "http://car.autohome.com.cn/zhaoche/pinpai/#pvareaid=103405"
    userAgent = "Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0"
    headers = {"User-Agent" : userAgent}
    request = urllib2.Request(url, headers = headers)
    html = urllib2.urlopen(request).read()
    tree = etree.HTML(html)
    for i in range(50):
        for j in range(50):
            try:
                p1 = "/html/body/div[3]/div[4]/div/div/div[" + str(i + 1) + "]/dl[" + str(j + 1) + "]/dt/p[2]/a/text()"
                p2 = "/html/body/div[3]/div[4]/div/div/div[" + str(i + 1) + "]/dl[" + str(j + 1) + "]/dd/ul/li/h4/a/text()" 
                carName = tree.xpath(p1)
                subCarName = tree.xpath(p2)
                line = carName[0].encode('utf-8') + '\t'
                for name in subCarName:
                    line = line + name.encode('utf-8') + '|'
                line = line.strip('|')
                line = line + '\n'
                fid.write(line)
            except Exception:
                continue
if __name__ == "__main__":
    carNameCrawl()