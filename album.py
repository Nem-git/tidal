import requests
import os
from thing import Thing

class Album(Thing):
    

    def __init__(self) -> None:
        self.request_url = "https://tidal.401658.xyz/album/"
        self.id = None
        self.date = None
        self.response = None
        self.cover = "https://resources.tidal.com/images/"
        self.artist_cover = self.cover
        self.songs = []
        self.path = None
        self.name = None
        self.artist_name = None


    def Infos(self):
        self.response = requests.get(self.request_url, params={"id" : self.id})
        while self.response.status_code != 200:
            self.response = requests.get(self.request_url, params={"id" : self.id})

        self.response = self.response.json()

        if self.response[0]["artist"]["picture"] != None:
            for _ in self.response[0]["artist"]["picture"].split("-"):
                self.artist_cover += f"{_}/"

        self.date = self.response[0]["releaseDate"].split("-")[0]
        self.cover = self.response[0]["cover"]

        for _ in self.response[0]["releaseDate"].split("-"):
            self.cover += f"{_}/"
        
        self.cover += "1280x1280.jpg"

        self.artist_name = self.response[0]['artist']['name']
        self.name = self.response[0]['title']

        self.path = f"../{self.artist_name}/{self.name}/"

        for i in self.response[1]["items"]:
            self.songs.append(i["item"]["id"])
        
        if not os.path.exists(f"{self.path}"):
            os.makedirs(self.path)
        else:
            pass
            #print(f"The path {self.path} already exists")