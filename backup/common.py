import os
import requests


class Common:

    def Send_request(request, paramaters) -> dict:
        response = requests.get(request, params=paramaters)
        while response.status_code != 200:
            if response.status_code == 404:
                break
            response = requests.get(request, params=paramaters)
        return response.json()

    def Verify_path(path) -> None:
        if not os.path.exists(path):
            os.makedirs(path)

    def Verify_string(text) -> str:
        if type(text) == str:
            for c in '*?<>"|':
                text = text.replace(c, "")
            for c in "'\\/:":
                text = text.replace(c, "-")
            return text

    def Clear(self) -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
