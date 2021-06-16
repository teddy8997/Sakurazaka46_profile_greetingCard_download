from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import os
import io
import sys
import warnings
import json
warnings.filterwarnings("ignore")

def get_html(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def downloadImg(memName, srcLink, savedir):
    if not os.path.isdir(savedir):
        os.makedirs(savedir)
    tmp = requests.get(srcLink)
    with open(savedir + "/" + memName +'.jpg', 'wb') as f:
                f.write(tmp.content)
    return "OK"


memList = ["03", "04", "06", "07", "08", "11", "14", "15", "18", "20", "21", "43", "53", "54", "55", "56", "44", "45", "46", "47", "57", "48", "50", "58", "51"]

for memNum in memList:
    url = "https://sakurazaka46.com/s/s46/artist/" + str(memNum) + "?ima=2449"
    html = get_html(url)
    res = bs(html)
    memPic = "https://sakurazaka46.com/" + res.find(class_="ph").find('img')['src']
    memName = res.find(class_="name").text.strip()
    PHOTO =  res.find(class_="part-cimg")
    memCard =  "https://sakurazaka46.com/" + res.find(class_="part-card").find('img')['src']
    if PHOTO is None:
        downloadImg(memName, memPic, "Pic")
        downloadImg(memName, memCard, "GreetingCard")
    else :
        Photo = "https://sakurazaka46.com/" + PHOTO.find('img')['src']
        downloadImg(memName, memPic, "Pic")
        downloadImg(memName, memCard, "GreetingCard")
        downloadImg(memName, Photo, "GreetingPHOTO")
    print(memName)



