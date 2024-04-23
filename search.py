from common import Common

class Search:

    def __init__(self) -> None:
        self.request_url = "https://tidal.401658.xyz/search/"
        self.response = None
        self.ids = []
        self.query = None
        self.liste = None


    def Artist(self) -> list:
        self.response = Common.Send_request(self.request_url, {"a" : self.query})

        for artist in self.response[0]["artists"]["items"]:
            print(f'{len(self.ids) + 1}. {artist["name"]} [{artist["id"]}]')
            self.ids.append(artist["id"])
        
        return self.ids
    
    def Album(self) -> list:
        self.response = Common.Send_request(self.request_url, {"al", self.query})

        for album in self.response["albums"]["items"]:
            print(f'{len(self.ids) + 1}. {album["title"]} - {album["artists"][0]} [{"id"}]')
            self.ids.append(album["id"])
        
        return self.ids


    def Choice(self) -> list:
        self.ids = []
        while len(self.ids) == 0:
            try:
                for number in input("\nTo choose, put a [space] between every number(ex: 1 2 5 6):\n").split(" "):
                    self.ids.append(int(number))

            except:
                self.ids = []
        
        return self.ids

