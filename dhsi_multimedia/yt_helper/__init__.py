# urllib
import urllib
import urllib3

# beautiful soup
from bs4 import BeautifulSoup

# pytube
from pytube import YouTube
from pytube import exceptions

QUERY_URL = 'https://www.youtube.com/results?search_query='
BASE_URL = 'https://www.youtube.com'


def get_urls(keyword):
    query = urllib.parse.quote(keyword)
    http = urllib3.PoolManager()
    res = http.request('GET', '{}{}'.format(QUERY_URL, query))
    html = res.data
    bs = BeautifulSoup(html, "html.parser")
    return ['{}{}'.format(BASE_URL, video['href']) for video in bs.findAll(attrs={'class': 'yt-uix-tile-link'})]


def download_videos(videos, directory):
    try:
        for video in videos:
            YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download(output_path=directory)
            print("Successfully downloaded {} to {}".format(video, directory))
    except exceptions.PytubeError as error:
        print(error)





