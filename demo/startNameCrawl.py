#coding=utf-8
'''
Created on 2016.10.30.

@author: ZakeXu

@百度阿拉丁：直接百度搜索框中输入对应query即可
'''
import urllib2
import json

def starNameCrawl():
    path = "../data/star_name"
    fid = open(path,'w')
    
    preUrl = "http://opendata.baidu.com/api.php?resource_id=28226&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E6%98%8E%E6%98%9F&sort_key=&sort_type=1"
    stat0 = ["", "男", "女"]
    stat1 = ["", "内地", "香港", "台湾", "日本", "韩国", "欧美"]
    starName = []
    userAgent = "Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0"
    headers = {"User-Agent":userAgent}
    pn = range(510)
    for s0 in stat0:
        for s1 in stat1:
            for p in pn:
                url = preUrl + "&stat0=" + s0 + "&stat1=" + s1 + "&stat2=&stat3=&pn=" + str(p * 12)
                request = urllib2.Request(url, headers = headers)
                data = urllib2.urlopen(request)
                json_data = json.load(data)
                for i in range(12):
                    try:
                        name = json_data['data'][0]['result'][i]['ename']
                        starName.append(name)
                    except Exception:
                        continue
    starName = list(set(starName))
    for name in starName:
        fid.write(name.encode('utf-8') + '\n')
if __name__ == "__main__":
    starNameCrawl()