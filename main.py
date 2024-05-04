from song import Song
from cover import Cover
from album import Album
from artist import Artist
from search import Search
from common import Common

def Artist_download(ids):
    for id in ids:
        artist = Artist()
        cover = Cover()
        artist.id = id
        artist.Infos()
        cover.Download(artist.response[0]["picture"], artist.path, "artist.jpg")
        print(f"Downloading all songs from {artist.name}")
        Album_download(artist.albums)
        

def Album_download(ids):
    album = Album()
    song = Song()
    cover = Cover()
    for id in ids:
        album.id = id
        album.Infos()
        print(f"{album.name.upper()} [{album.id}]")
        Track_download(album.songs)
        cover = Cover()
        album = Album()

def Track_download(ids):
    for id in ids:
        song = Song()
        cover = Cover()
        song.quality = "HI_RES_LOSSLESS"
        song.id = id
        song.Infos()
        print(song.name.lower())
        cover.Download(song.album_cover, song.path, "cover.jpg")
        song.Download()
        cover.Download(song.artist_cover, f"../{song.artist_name}/", "artist.jpg")
        song.Tag()

def Cover_download(id, path, name):
    cover = Cover()
    Common.Verify_path(path)
    cover.id = id
    cover.Download()


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
