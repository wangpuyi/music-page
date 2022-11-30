import requests
import re
import os

def crawler(filename,url):
    # filename = 'music_飙升榜\\'

    if not os.path.exists(filename):
        os.mkdir(filename)

    # url = 'https://music.163.com/discover/toplist'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
    }
    responce = requests.get(url=url,headers=headers)

    html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', responce.text)
    print(html_data)

    for num_id,title in html_data:
        music_url = f'https://music.163.com/song/media/outer/url?id={num_id}.mp3'
        music_content = requests.get(url=music_url,headers=headers).content
        with open(filename + num_id + '.mp3', mode='wb') as f:
            print(num_id,title)
            f.write(music_content)


crawler('music_原创榜\\','https://music.163.com/discover/toplist?id=2884035')