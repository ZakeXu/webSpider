#coding=utf-8
'''
Created on 2016.10.30.

@author: ZakeXu

@百度阿拉丁：直接百度搜索框中输入对应query即可
'''
import urllib2
import json

def animalNameCrawl():
    path = "../data/animal_name"
    fid = open(path, 'w')
    
    preUrl = "http://opendata.baidu.com/api.php?format=json&ie=utf-8&oe=utf-8&query="
    animal = ["狗", "猫", "仓鼠", "松鼠", "鸟", "兔", "蛇"]
    postUrl = "&resource_id=6829&rn=12&from_mid=1&pn="
    for query in animal:
        for i in range(20):
            url = preUrl + query + postUrl + str(i * 12)
            data = urllib2.urlopen(url)
            json_data = json.load(data)
            for i in range(12):
                try:
                    name = json_data['data'][0]['disp_data'][i]['word']
                    fid.write(name.encode('utf-8') + '\n')
                except Exception:
                    continue
if __name__ == "__main__":
    animalNameCrawl()