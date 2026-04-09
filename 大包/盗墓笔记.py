import requests
url="http://www.daomubiji.com/"
headers = {
    "User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
response = requests.get(url,headers=headers)
with open("daomu.html", "w", encoding="utf-8") as a:
    a.write(response.content.decode("utf-8"))