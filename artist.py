from common import Common

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


    def Infos(self) -> None:

        self.response = Common.Send_request(self.request_url, {"f" : self.id})

        self.liste = self.response[0]["rows"][0]["modules"][0]["pagedList"]["items"]

        for i in self.liste:
            self.albums.append(i["id"])
        try:
            self.name = Common.Verify_string(Common.Send_request(f"https://tidal.401658.xyz/artist/", {"id" : self.id})[0]["name"])
        except:
            self.name = Common.Verify_string(Common.Send_request(f"https://tidal.401658.xyz/artist/", {"id" : self.id})[0]["title"])

        Common.Verify_path(f"../{self.name}/")