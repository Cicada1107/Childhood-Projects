'''To be imported to the main bot code; Gets memes, treats them as objects and sends them to chat on command'''
#To get more than just 20 memes, use more than one website.
#Implement a sort or filter based on likes receieved by the meme to get the good ones only

import requests, re
from bs4 import BeautifulSoup

#Possible websites: 9gag, meemdroid

class Meme:
    '''A meme data type object'''
    def __init__(self, caption, src, queue_position, likes):
        self.src = src
        self.queue_position = queue_position
        self.caption = caption
        self.likes = likes #for filter, find a way to extract the like percentage
        


def load_memes(payload: dict, query: str = None):
    '''Gets n number of memes from memedroid with an optional search query specified by user, returns the html tree'''
    #payload is simply the query string denoting the page number.
    search = {"query": query} #For searching a query specified by the user
    if query != None:
        extract = requests.get(url = "https://www.memedroid.com/search", params = search)
    else:
        extract = requests.get(url = "https://www.memedroid.com/memes/top/day", params = payload)
    soup = BeautifulSoup(extract.content, 'html.parser')
    return soup
    
def get_memes(n: int = 10, search: str = None):
    '''Loads required number of subpages in the website till n number of memes are accumulated; returns list of n memes as required'''
    memes = []
    q = 0
    page = 0
    if page == "1": payload = None
    if search == None:
        while len(memes) != n:
            page += 1
            payload = {"page": str(page)}
            soup = load_memes(query = search, payload = payload)
            for i in soup.find_all(name = 'img', attrs = {"class": "img-responsive grey-background"}):  #Filtering out all 'img' tags with class of the type of meme content on the website
                q += 1
                meme = Meme(src = i["src"], queue_position = q, caption = i["alt"], likes = "likes counter yet to be implimented")#Get the like percentage somehow and make it so that it is always above 75 or 80
                memes.append(meme)
                if len(memes) == n: return memes
    else:
        soup = load_memes(query = search, payload = None)
        for i in soup.find_all(name = 'img', attrs = {"class": "img-responsive grey-background"}):  #Filtering out all 'img' tags with class of the type of meme content on the website
                q += 1
                meme = Meme(src = i["src"], queue_position = q, caption = i["alt"], likes = 0)#Get the like percentage somehow and make it so that it is always above 75 or 80
                memes.append(meme)
                return memes
