import json
import os
import requests
import wget
import time

saveDir = 'image'

heroListUrl = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
resp = requests.get(heroListUrl)
resp.encoding = 'utf-8'
resp = resp.text
heroList = json.loads(resp)

heroes = heroList['hero']

for hero in heroes:
    heroId = hero['heroId']
    heroName = hero['name']

    savePath = os.path.join(saveDir, heroName)
    
    if not os.path.exists(savePath):
        os.makedirs(savePath)

    url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
    url = url.format(heroId)
    

    resp = requests.get(url) 
    resp.encoding = 'utf-8'
    resp = resp.text
    hero = json.loads(resp)

    skins = hero['skins']

    for skin in skins:
        imgUrl = skin['mainImg']
        skinName = skin['name'].replace("/", " ")
        if imgUrl == '' or skinName == '':
            continue
        
        saveName = f'{skinName}.jpg'
        print(imgUrl)
        
        if not os.path.exists(os.path.join(savePath, saveName)):
            wget.download(imgUrl, os.path.join(savePath, saveName))
        time.sleep(0.1)