from song import Song
from cover import Cover
from album import Album
from artist import Artist
from search import Search
from common import Common
import os

def Artist_download(ids):
    for id in ids:
        artist = Artist()
        artist.id = id
        artist.Infos()
        print(f"Downloading all songs from {artist.name}")
        Album_download(artist.albums)
        

def Album_download(ids):
    album = Album()
    song = Song()
    cover = Cover()
    for id in ids:
        album.id = id
        album.Infos()
        print(album.name.upper())
        #song.artist_cover = album.artist_cover
        if not os.path.exists(f"{song.path}cover.jpg"):
            cover.id = album.id + 1
            cover.path = album.path
            cover.Download()
        Track_download(album.songs)
        cover = Cover()
        album = Album()

def Track_download(ids):
    for id in ids:
        song = Song()
        song.quality = "HI_RES_LOSSLESS"
        song.id = id
        song.Infos()
        print(song.name.lower())
        song.Download()
        song.Tag()

def Cover_download(ids):
    cover = Cover()
    for id in ids:
        pass


if __name__ == "__main__":
    common = Common()
    search = Search()
    common.Clear()
    
    search_type = None
    query = None
    while type(search_type) != int:
        try:    
            search_type = int(input("What kind of search?\n\n1. Search artist\n2. Search album\n3. Search track\n4. Search cover\n"))
        except:
            print("Please enter a valid number\n")

    common.Clear
    query_id = int(input("1. Search query\n2. Search IDs\n"))
    ids = []

    if query_id == 1:
        query = input("Query:\n")
        search.query = query

    
    if query_id == 2:
        for number in input("IDs ([space] between every ID (ex: 1 4 5)):\n").split(" "):
            ids.append(int(number))
    
    common.Clear()

    if search_type == 1:
        if query_id == 1:
            search.liste = search.Artist()
            for number in search.Choice():
                ids.append(search.liste[number - 1])

        search = Search()
        Artist_download(ids)

        
    if search_type == 2:
        if query_id == 1:
            search.liste = search.Album()
            for number in search.Choice():
                ids.append(search.liste[number - 1])
    
        search = Search()
        Album_download(ids)
        
    if search_type == 3:
        if query_id == 1:
            search.liste = search.Track()
            for number in search.Choice():
                ids.append(search.liste[number - 1])
        
        search = Search()
        Track_download(ids)
        
    if search_type == 4:
        if query_id == 1:
            search.liste = search.Cover()
            for number in search.Choice():
                ids.append(search.liste[number - 1])
        
        search = Search()
        Cover_download(ids)
