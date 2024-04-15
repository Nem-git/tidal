from common import Common

class 

class Search:

    def __init__(self) -> None:
        self.request_url = "https://tidal.401658.xyz/search/"
        self.id = None
        self.name = None
        self.query = None
        self.ids = []

    

    def Artist(self) -> list:
        self.request_url = Common.Send_request(self.request_url, {"a" : self.query})

        for artist in self.request_url[0]["artist"]["items"]:
            self.ids.append(f'{artist + 1}. {artist["name"]} {artist["id"]}')