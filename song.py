import requests
from mutagen import flac, id3
from common import Common
from album import Album

class Song(Common):

    def __init__(self) -> None:
        self.download_url = "https://tidal.401658.xyz/track/"
        self.search_url = "https://tidal.401658.xyz/search/"
        self.artist_name = Album().artist_name
        self.artist_cover = None
        self.album_name = Album().name
        self.album_cover = None
        self.name = None
        self.number = None
        self.date = None
        self.url = None
        self.path = None
        self.id = None
        self.quality = None
        self.response = None
        self.query = None

    
    def Infos(self) -> None:

        self.response = Common.Send_request(self.download_url, {"id" : self.id, "quality" : self.quality})

        self.name = Common.Verify_string(self.response[0]["title"])
        self.artist_cover = self.response[0]["artist"]["picture"]
        self.album_cover = self.response[0]["album"]["cover"]
        self.number = f"{self.response[0]['trackNumber']:02}"
        self.url = self.response[2]["OriginalTrackUrl"]

        if self.artist_name == None:
            self.artist_name = self.response[0]["artist"]["name"]
        if self.album_name == None:
            self.album_name = self.response[0]["album"]["title"]
        self.path = f"../{self.artist_name}/{self.album_name}/"
    
    def Download(self) -> None:

        Common.Verify_path(self.path)
        

        with open(f'{self.path}{self.number} {self.name}.{self.url.split(".")[4].split("?")[0]}', "wb") as track:
            self.response = requests.get(self.url)
            while self.response.status_code != 200:
                self.response = requests.get(self.url)
            track.write(self.response.content)
    
    def Tag(self) -> None:
        try:
            track = flac.FLAC(f"{self.path}{self.number} {self.name}.flac")

            track.add_tags()
            track.tags["ALBUM"] = self.album_name
            track.tags["ARTIST"] = self.artist_name
            track.tags["COMMENT"] = f"QUALITY: {self.quality}"
            track.tags["TITLE"] = self.name
            track.tags["TRACKNUMBER"] = self.number

            try:
                self.album_cover = flac.Picture()

                with open(f"{self.path}{self.album_name}.jpg", "rb") as _:
                    self.album_cover.data = _.read()

                self.album_cover.type = id3.PictureType.COVER_FRONT
                
                if self.artist_cover is not None:
                    self.artist_cover = flac.Picture()

                    with open(f"../{self.artist_name}/{self.artist_name}.jpg", "rb") as _:
                        self.artist_cover.data = _.read()
                    
                    self.artist_cover.type = id3.PictureType.ARTIST
                    self.artist_cover.mime = u"image/jpeg"
                    track.add_picture(self.artist_cover)

                self.album_cover.mime = u"image/jpeg"
                self.album_cover.width = 1280
                self.album_cover.height = 1280
                track.add_picture(self.album_cover)
            except:
                pass

            track.save()
        
        except:
            print("NOT A FLAC FILE")