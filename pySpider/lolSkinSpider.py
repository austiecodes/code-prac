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
    resp.encoding()
    resp = resp.text

    savePath = os.path.join(saveDir, heroName)
    if not os.path.exists(savePath):
        os.makedirs(savePath)

    hero = json.loads(resp)
    skins = hero['skins']
    for skin in skins:
        mainImg = skin['mainImg']
        skinName = skin['name'].replace("/", " ")
        if mainImg == " " or skinName == " ":
            continue
        #print(imgName)
        saveName = f'{skinName}.jpg'
        if not os.path.exists(os.path.join(saveDir, saveName)):
            wget.download(mainImg, os.path.join(saveDir, f'{skinName}.jpg'))
        time.sleep(0.1)