import requests
import os
from thing import Thing

class Cover(Thing):
    def __init__(self) -> None:

        self.request_url = "https://tidal.401658.xyz/cover/"
        self.url = None
        self.id = None
        self.path = None
        self.response = None

    def Download(self) -> None:

        self.response = requests.get(self.request_url, params={"id" : self.id})
        while self.response.status_code != 200:
            self.response = requests.get(self.request_url, params={"id" : self.id})

        self.response = self.response.json()
        self.url = self.response[0]["1280"]

        with open(f"{self.path}cover.jpg", "wb") as f:
            self.response = requests.get(self.url)
            while 200 != self.response.status_code:
                self.response = requests.get(self.url)
            f.write(self.response.content)
        
