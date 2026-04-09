import requests
import csv
from lxml import etree
data = []

url = 'https://www.tripadvisor.com/Restaurant_Review-g255060-d12666547-Reviews-Jade_Temple-Sydney_New_South_Wales.html'
headers = {
    'user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
html = etree.HTML(response.content)
res = html.xpath('//*[@id="taplc_location_reviews_list_resp_rr_resp_0"]/div')
for tr in res:
    itme = {}
    itme['ID'] = tr.xpath('./div')
