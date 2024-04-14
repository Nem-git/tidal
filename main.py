from song import Song
from cover import Cover
from album import Album
from artist import Artist
import os

song = Song()
album = Album()
cover = Cover()
artist = Artist()

if __name__ == "__main__":

    artist.id = 36212
    artist.Infos()
    
    for al in artist.albums:
        
        print(al)

        album.id = al

        album.Infos()
    
        song.artist_cover = album.artist_cover

        for id in album.songs:
            song.artist_name = artist.name
            song.album_name = album.name
            song.quality = "HI_RES_LOSSLESS"
            song.id = id
            song.Infos()
            song.Download()

            if not os.path.exists(f"{song.path}cover.jpg"):
                cover.id = album.id + 1
                cover.path = album.path
                cover.Download()
            else:
                pass

            song.Tag()
            
            cover = Cover()
            song = Song()

        album = Album()

    artist = Artist()


    
