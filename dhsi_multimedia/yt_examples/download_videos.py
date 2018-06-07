# yt helper
from yt_helper import get_urls, download_videos

# IO Parser
from io_utils import IOParser

if __name__ == '__main__':
    parser = IOParser()
    query = parser.input
    directory = parser.output

    urls = get_urls(query)
    download_videos(urls, directory)