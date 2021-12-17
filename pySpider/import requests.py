import requests, json, wget,os

heroListUrl = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
resp = requests.get(heroListUrl)
resp.encoding = "utf-8"
resp = resp.text

heroList = json.loads(resp)

save_path = "image"

heroes = heroList['hero']
for hero in heroes:
    heroId = hero[heroId]
    heroName = hero['name']

    url = "https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js"
    url = url.format(heroId)
    resp = requests.get(url)
    resp.encoding = "utf-8"
    resp = resp.text
    savepath = os.path.join(save_path, heroName)
    if not os.path.exists(savepath):
        os.makedirs
  
    obj = json.loads(resp)
    skins = obj['skins']
    for skin in skins:
        mainImg = skin['mainImg']
        wget.download(mainImg, savepath)





    print(url)




