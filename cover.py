import requests
from common import Common
import os

class Cover():
    request_url = "https://tidal.401658.xyz/cover/"
    url = None
    response = None

    def Download(self, id, path, name) -> None:

        try:
            if not os.path.exists(path + name):
                Common.Verify_path(path)
                self.url = "https://resources.tidal.com/images/" + id.replace("-", "/") + "/750x750.jpg"
                print(self.url)
                with open(f"{path + name}", "wb") as f:
                    self.response = requests.get(self.url)
                    while self.response.status_code != 200:
                        if self.response.status_code == 404:
                            break
                        self.response = requests.get(self.url)
                    f.write(self.response.content)
        except:
            print(f"No image to put in {path + name}")
        
