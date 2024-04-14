import requests
import os
from thing import Thing

class Artist(Thing):

    def __init__(self) -> None:

        self.request_url = "https://tidal.401658.xyz/search/"
        self.id = None
        self.name = None
        self.response = None
        self.path = None
        self.liste = None
        self.albums = []

    def Infos(self) -> None:
        self.response = requests.get(self.request_url, params={"f" : self.id})
        while self.response.status_code != 200:
            self.response = requests.get(self.request_url, params={"f" : self.id})
        
        self.response = self.response.json()

        self.liste = self.response[0]["rows"][0]["modules"][0]["pagedList"]["items"]


        for i in self.liste:
            self.albums.append(i["id"])
        for character in "\/":
            self.name = self.response[0]["rows"][0]["modules"][0]["pagedList"]["items"][0]["artists"][0]["name"].replace(character, "")
        
        self.path = f"../{self.name}/"

        if not os.path.exists(f"{self.path}"):
            os.makedirs(self.path)
        else:
            pass
            #print(f"The path {self.path} already exists")
