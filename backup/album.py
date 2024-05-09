from common import Common


class Album:

    def __init__(self) -> None:
        self.request_url = "https://tidal.401658.xyz/album/"
        self.id = None
        self.date = None
        self.response = None
        self.cover = None
        self.artist_cover = self.cover
        self.songs = []
        self.path = None
        self.name = None
        self.artist_name = None

    def Infos(self) -> None:

        self.response = Common.Send_request(self.request_url, {"id": self.id})

        if self.response[0]["artist"]["picture"] != None:
            self.cover = self.response[0]["cover"]

        self.date = self.response[0]["releaseDate"].split("-")[0]

        self.name = Common.Verify_string(self.response[0]["title"])

        for i in self.response[1]["items"]:
            self.songs.append(i["item"]["id"])

        if self.artist_name == None:
            self.artist_name = Common.Verify_string(self.response[0]["artist"]["name"])

        self.path = f"../{self.artist_name}/{self.name}/"
        Common.Verify_path(self.path)
