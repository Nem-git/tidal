import requests
from mutagen.flac import FLAC
import os

class Song:
    request_url = "https://tidal.401658.xyz/track/"
    artist_name = None
    artist_cover = None
    album_name = None
    album_cover = None
    name = None
    number = None
    date = None
    url = None
    path = None
    id = None
    quality = None
    response = None
    
    def Infos(self) -> None:
        self.response = requests.get(self.request_url, params={"id" : self.id, "quality" : self.quality})
        while self.response.status_code != 200:
            self.response = requests.get(url, params={"id" : self.id, "quality" : self.quality})
        
        self.response = self.response.json()
        
        self.artist_name = self.response[0]["artist"]["name"]
        self.artist_cover = self.response[0]["artist"]["picture"]
        self.album_name = self.response[0]["album"]["title"]
        self.album_cover = self.response[0]["album"]["cover"]
        self.name = self.response[0]["title"]
        self.number = f'{self.response[0]["trackNumber"]:02}'
        self.url = self.response[2]["OriginalTrackUrl"]
        self.path = f"../{self.artist_name}/{self.album_name}/"
    
    def Download(self) -> None:

        if not os.path.exists(self.path):
            os.makedirs(self.path)
        else:
            print(f"The path {self.path} already exists")
        
        with open(f"{self.path}{self.number} {self.name}.flac", "wb") as f:
            self.response = requests.get(self.url)
            while self.response.status_code != 200:
                self.response = requests.get(self.url)
            f.write(self.response.content)
    
    def Tag(self) -> None:
        f = FLAC(f"{self.path}{self.number} {self.name}.flac")
        print(f.tags)
        f.add_tags()
        f.tags["ALBUM"] = self.album_name
        f.tags["ARTIST"] = self.artist_name
        f.tags["COMMENT"] = f"QUALITY: {self.quality}"
        f.tags["TITLE"] = self.name
        f.tags["TRACKNUMBER"] = self.number
        f.save()

        f = FLAC(f"{self.path}{self.number} {self.name}.flac")
        print(f.tags)



        print(f.tags)
        





#song_response = requests.get(f"{url}track/?id={song_id}&quality={song_quality}").json()
#song_path = f"../{artist_name}/{artist_name} - {song_response[0]['album']['title']} ({release_year})/"

#if not os.path.exists(song_path):
#    os.makedirs(song_path)
#else:
#    "Something doesnt work with the path"
    
#with open(f"{song_path}{artist_name} - {song_response[0]['title']}.flac", "wb") as f:
#    song_link = requests.get(song_response[2]['OriginalTrackUrl'])
#    while 200 != song_link.status_code:
#        song_link = requests.get(song_response[2]['OriginalTrackUrl'])
#    f.write(song_link.content)
        

