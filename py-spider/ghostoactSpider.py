import requests
 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
cookies = {'cookie': '1_be5452ad79c993ce5fe62b72d6f24fe61635164021592'}
 
url = 'https://www.ghostoact.com/arts/models/cycle'
r = requests.get(url, cookies = cookies, headers = headers)
