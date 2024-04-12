import requests
from mutagen import flac
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
            self.response = requests.get(self.request_url, params={"id" : self.id, "quality" : self.quality})
        
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

        if not os.path.exists(f"{self.path}{self.number} {self.name}.flac"):
            os.makedirs(self.path)
        else:
            print(f"The path {self.path} already exists")
        
        with open(f"{self.path}{self.number} {self.name}.flac", "wb") as f:
            self.response = requests.get(self.url)
            while self.response.status_code != 200:
                self.response = requests.get(self.url)
            f.write(self.response.content)
    
    def Tag(self) -> None:
        f = flac.FLAC(f"{self.path}{self.number} {self.name}.flac")
        print(f.tags)
        f.add_tags()
        f.tags["ALBUM"] = self.album_name
        f.tags["ARTIST"] = self.artist_name
        f.tags["COMMENT"] = f"QUALITY: {self.quality}"
        f.tags["TITLE"] = self.name
        f.tags["TRACKNUMBER"] = self.number
        f.save()
        f.add_picture(f"{self.path}cover.jpg")
        pic = flac.Picture()
        with open(f"{self.path}cover.jpg", "rb") as cover:
            pic.data = cover.read()
        pic.mime = u"image/jpeg"
        pic.width = 1280
        pic.height = 1280
        


        f = flac.FLAC(f"{self.path}{self.number} {self.name}.flac")
        print(f.tags)