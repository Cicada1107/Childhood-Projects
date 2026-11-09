import re, bs4, requests
from youtube_dl import YoutubeDL as yt


class Video:
    """A youtube video"""
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        #self.title = self.title()

    def info(self):
        """Returns the title of the video"""
        with yt({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
            try: get(self.url)
            except: info = ydl.extract_info("ytsearch:{}".format(self.url), download=False)['entries'][0]
            else: info = ydl.extract_info(self.url, download=False)
        return (info['title'], info['description'])

    def is_rickroll(self):
        """Returns True if the youtube video on the given url is a rickroll"""
        flag = re.match(r".*(Rickroll|Never gonna give you up)\s+.*", self.info()[0], re.IGNORECASE) or re.match(r".*(Rickroll|Never gonna give you up)\s+.*", self.info()[1], re.IGNORECASE)
        return flag

