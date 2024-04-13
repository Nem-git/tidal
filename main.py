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
    artist = Artist()

    artist.id = 7162333
    artist.Infos()

    for al in artist.albums:
        album = Album()

        album.id = al

        album.Infos()

        #cover.id = album.id + 1
        #cover.path = album.path
        #cover.Download()
    
        song.artist_cover = album.artist_cover

        for id in album.songs:
            song = Song()
            print(id)
            song.quality = "HI_RES_LOSSLESS"
            song.id = id
            song.Infos()
            song.Download()

            if not os.path.exists(f"{song.path}cover.jpg"):
                cover = Cover()
                cover.id = album.id + 1
                cover.path = album.path
                cover.Download()
            else:
                pass

            song.Tag()




    
