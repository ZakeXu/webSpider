#coding:utf-8
'''
Created on 2016.10.30

@author: ZakeXu

@动漫影院：http://www.dmyy.cc/
'''
import urllib2
from lxml import etree
import json

def cartoonSchemaCrawl():
    path = "../data/cartoon_schema"
    fid = open(path,'w')
    
    for i in range(30000):
        try:
            url = "http://www.dmyy.cc/DongMan/" + str(i + 1) + "/"
            userAgent = "Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0"
            headers = {"User-Agent" : userAgent}
            request = urllib2.Request(url, headers = headers)
            html = urllib2.urlopen(request).read()
            tree = etree.HTML(html)
            
            cartoonSchema = {}
            cartoonSchema['id'] = str(i+1)
            cartoonSchema['title'] = tree.xpath("//div[@class='title']/h1/text()")
            cartoonSchema['author'] = tree.xpath("//div[@class='info']/p[2]/text()")
            cartoonSchema['language'] = tree.xpath("//div[@class='info']/p[3]/text()")
            cartoonSchema['type'] = tree.xpath("//div[@class='info']/p[5]/a/text()")
            cartoonSchema['actor'] = tree.xpath("//div[@class='info']/p[6]/a/text()")
            cartoonSchema['introduction'] = tree.xpath("//div[@id='intro1']")[0].xpath("string(.)")
            cartoonSchema['year'] = tree.xpath("//div[@class='info']/p[4]/text()") 
            if len(cartoonSchema['title']) > 0:
                fid.write(json.dumps(cartoonSchema, ensure_ascii = False).encode('utf-8', 'ignore') + '\n')
        except Exception:
            continue
if __name__ == "__main__":
    cartoonSchemaCrawl()

