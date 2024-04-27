from common import Common
import requests

class Artist:

    def __init__(self) -> None:

        self.request_url = "https://tidal.401658.xyz/artist/"
        self.id = None
        self.name = None
        self.response = None
        self.liste = None
        self.albums = []
        self.search_albums = []
        self.query = None
        self.cover = None
        self.path = None


    def Infos(self) -> None:

        self.response = Common.Send_request(self.request_url, {"f" : self.id})        

        self.liste = self.response[0]["rows"][0]["modules"][0]["pagedList"]["items"]

        for i in self.liste:
            self.albums.append(i["id"])
        
        try:
            self.name = Common.Verify_string(Common.Send_request(f"https://tidal.401658.xyz/artist/", {"id" : self.id})[0]["name"])
        except:
            self.name = Common.Verify_string(Common.Send_request(f"https://tidal.401658.xyz/artist/", {"id" : self.id})[0]["title"])
        self.path = f"../{self.name}/"
        Common.Verify_path(self.path)

        print(self.response[1][0])
        try:
            self.cover = self.response[1][0]["750"]
            print(self.cover)
            with open(f'{self.path}{self.name}.jpg') as c:
                self.response = requests.get(self.cover)
                while self.response.status_code != 200:
                    self.response = requests.get(self.cover)
                c.write(self.response.content)
        except:
            print("No artist cover")
        
