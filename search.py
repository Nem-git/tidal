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
            for char in "\/*":
                text = text.replace(char, "")
            return text
    
    def Search_choice() -> list:
        search = Search()
        url = "https://tidal.401658.xyz/search/"
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
        search_type = None
        while type(search_type) != int:
            try:    
                search_type = int(input("What kind of search?\n\n1. Search artist\n2. Search album\n3. Search track\n4. Search cover\n"))
            except:
                print("Please enter a valid number\n")
        
        if search_type == 1:
            search.Artist()
        
        if search_type == 2:
            search.Album()
        
        if search_type == 3:
            search.Track()
        
        if search_type == 4:
            search.Cover()
    
    def Choice(liste) -> list:
        print("\n")
        for item in liste:
            print(f"{'a'}")

class Search:

    def __init__(self) -> None:
        self.request_url = "https://tidal.401658.xyz/search/"
        self.response = None
        self.id = None
        self.name = None
        self.query = "Kanye West"
        self.ids = []

    

    def Artist(self) -> list:
        self.response = Common.Send_request(self.request_url, {"a" : self.query})
        
        for artist in self.response[0]["artists"]["items"]:
            self.ids.append(f'{len(self.ids) + 1}. {artist["name"]} {artist["id"]}')
            print(self.ids[-1])
        
        
        

        
search = Search()
common = Common()

Common.Search_choice()

