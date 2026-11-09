'''using an unofficial 9GAG Python API to get articles from 9GAG in the chat directly'''
'''DEPRECATED. This module doesn't seem to work anymore. So this program doesn't work either.'''

import pyninegag

class Gag:
    '''A meme data type object'''
    def __init__(self, caption, src, queue_position, likes, media_type):
        self.src = src
        self.queue_position = queue_position
        self.caption = caption
        self.likes = likes #for filter, find a way to extract the like percentage
        self.media_type = media_type

    def delete(self):
        pass

def get_gags(n = 1):
    '''Gets the gags from the main page of 9GAG and return them in the form of gag data type elements in a list'''
    gags = []
    extract = pyninegag.get_articles(pyninegag.BASE_URL)
    q = 0
    for i in extract:
        q += 1
        gag = Gag(caption = i["title"], src = i["data"]["url"], queue_position = q, likes = i["votes"], media_type = i["data"]["type"])
        gags.append(gag)
    return gags