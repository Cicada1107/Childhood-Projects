#Anti_rickroll

"""Detects the mention of rickroll in the title or description of a given youtube video.
Made by Arijit Dubey"""


'''
Helpful links:
1. difference between urllib.request and requests module in python
https://www.google.com/search?channel=crow5&client=firefox-b-d&q=what+is+the+difference+between+requests+and+urllib.request+in+python
2. Using Python and beautiful soup to get video tittles in youtube
https://stackoverflow.com/questions/62530786/using-requests-and-beautifulsoup-to-get-youtube-video-titles-sometimes-errors-an
3. Pretty printing in python using beautiful soup in python using requests module
https://www.geeksforgeeks.org/pretty-printing-in-beautifulsoup/
4.https://www.geeksforgeeks.org/python-obtain-title-views-and-likes-of-youtube-video-using-beautifulsoup/
5. How to use parameters for classes
https://www.quora.com/Why-do-python-classes-always-require-a-self-parameter
'''

'''
Future scope:
1. Add support for other platforms capable of riockrolling if possible using requests and beautiful soup.
'''

import re
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
