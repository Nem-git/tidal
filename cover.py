import requests
from common import Common

class Cover():
    request_url = "https://tidal.401658.xyz/cover/"
    url = None
    id = None
    path = None
    response = None

    def Download(self) -> None:

        self.response = Common.Send_request(self.request_url, {"id" : self.id})

        try:
            self.url = self.response[0]["1280"]
            with open(f"{self.path}cover.jpg", "wb") as f:
                self.response = requests.get(self.url)
                while self.response.status_code != 200:
                    if self.response.status_code == 404:
                        break
                    self.response = requests.get(self.url)
                f.write(self.response.content)
        except:
            print("No cover for this album")
        
