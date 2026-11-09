#spotify sync

import spotipy, asyncio
from spotipy.oauth2 import SpotifyClientCredentials
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')
client_id = config['Spotify']['client_id']
client_secret = config['Spotify']['client_secret']

auth_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


class Album:
    '''An album object in spotify'''
    def __init__(self, album_id: str):
        self.id = album_id
        album = sp.album(self.id)
        self.title = album["name"]
        self.artist = album["artists"][0]["name"]

    def view(self):
        '''Gives a view of all the songs and their respective duration present in a album'''
        __temp = album["tracks"]["items"]
        view = [track["name"] for track in __temp]
        return view

class Playlist:
    '''A playlist object in spotify'''
    def __init__(self, playlist_id: str):
        self.id = playlist_id
        playlist = sp.playlist(self.id)
        self.owner = playlist["owner"]["display_name"]

    def view(self):
        '''Gives a view of all the songs and their respective artists present in a playlist'''
        __temp = playlist["tracks"]["items"]
        view = [{track["track"]["artists"][0]["name"]: track["track"]["name"]} for track in __temp]
        return view

    def artists(self):
        '''Returns the various artists in the playlist'''
        __temp = playlist["tracks"]["items"]
        artists = []
        [artist.append(track["track"]["artists"][0]["name"]) for track in __temp]
        return artists
