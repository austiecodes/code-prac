import json
import os
import requests
import wget
import time

heroListUrl = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
resp = requests.get(heroListUrl)
resp.encoding = 'utf-8'
resp = resp.text

List = json.loads(resp)

saveDir = 'image'

heroes = List['hero']
for hero in heroes:
    heroId = hero['heroId']
    heroName = hero['name']

    url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
    url = url.format(heroId)

    resp = requests.get(url) 
    resp = resp.text

    savePath = os.path.join(saveDir, heroName)
    if not os.path.exists(savePath):
        os.makedirs(savePath)

    hero = json.loads(resp)
    skins = hero['skins']
    for skin in skins:
        mainImg = skin['mainImg']
        imgName = skin['name']
        file =  os.path("image/{}.jpg")
        file = file.format(imgName)
        #print(imgName)
        if not file.exists():
            if mainImg == " ":
                continue
            wget.download(mainImg, savePath)
        time.sleep(0.1)