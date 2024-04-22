from song import Song
from cover import Cover
from album import Album
from artist import Artist
from search import Search
import os

song = Song()
album = Album()
cover = Cover()
artist = Artist()
search = Search()


if __name__ == "__main__":

#    artist.id = 9127 #7589458
#    artist.Infos()
#    
#    for al in artist.albums:

#        album.id = al
#        album.artist_name = artist.name
#        album.Infos()
#        print(album.name)
    
#        song.artist_cover = album.artist_cover

#        if not os.path.exists(f"{song.path}cover.jpg"):
#            cover.id = album.id + 1
#            cover.path = album.path
#            cover.Download()
        
#        for id in album.songs:
#            song.artist_name = artist.name
#            song.album_name = album.name
#            song.quality = "HI_RES_LOSSLESS"
#            song.id = id
#            song.Infos()
#            song.Download()

#            song.Tag()
            
#            song = Song()
        
#        cover = Cover()

#        album = Album()

#    artist = Artist()


    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    search_type = None
    query = None
    while type(search_type) != int:
        try:    
            search_type = int(input("What kind of search?\n\n1. Search artist\n2. Search album\n3. Search track\n4. Search cover\n"))
            query = input("Query:\n")
        except:
            print("Please enter a valid number\n")
    
    if search_type == 1:
        search.query = query
        search.liste = search.Artist()
        numbers = search.Choice()
        ids = []
        for number in numbers:
            ids.append(search.liste[number - 1])
        for id in ids:
            artist.id = id #9127 #7589458
            artist.Infos()
            
            for al in artist.albums:

                album.id = al
                album.artist_name = artist.name
                album.Infos()
                print(album.name)
            
                song.artist_cover = album.artist_cover

                if not os.path.exists(f"{song.path}cover.jpg"):
                    cover.id = album.id + 1
                    cover.path = album.path
                    cover.Download()
                
                for id in album.songs:
                    song.artist_name = artist.name
                    song.album_name = album.name
                    song.quality = "HI_RES_LOSSLESS"
                    song.id = id
                    song.Infos()
                    song.Download()
                    song.Tag()

                    song = Song()

                cover = Cover()
                album = Album()

            artist = Artist()

        search = Search()
        
    if search_type == 2:
        self.Album()
        
    if search_type == 3:
        self.Track()
        
    if search_type == 4:
        self.Cover()
