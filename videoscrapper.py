from bs4 import BeautifulSoup
from pytube import YouTube
import sys


def Youtube(url):
    if "playlist" in url:
        if sys.version_info[0] == 3:
            from urllib.request import urlopen
        else:
            # Not Python 3 - today, it is most likely to be Python 2
            # But note that this might need an update when Python 4
            # might be around one day
            from urllib import urlopen


        uuu = urlopen(url).read()
        soup = BeautifulSoup(uuu, 'html.parser')
        a = soup.find_all("td", class_="pl-video-title")
        print(len(a))
        for i in a:
            links = i.find('a').get('href')
            print('links',links," ",len(a))
            yt = YouTube("https://www.youtube.com" + links)
            print(yt.streams.first().download())
            continue
        print('complete')
    elif 'watch' in url:
        print(url)
        yt = YouTube(url)
        print(yt.streams.first().download())
    else:
        print('url wrong')

a = sys.argv[-1]
Youtube(a)
