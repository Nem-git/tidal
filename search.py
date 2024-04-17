import os
import requests
from common import Common

class Search:

    def __init__(self) -> None:
        self.request_url = "https://tidal.401658.xyz/search/"
        self.response = None
        self.id = None
        self.name = None
        self.query = None
        self.ids = []

    

    def Artist(self) -> int:
        self.response = Common.Send_request(self.request_url, {"a" : self.query})

        for artist in self.response[0]["artists"]["items"]:
            self.ids.append(f'{len(self.ids) + 1}. {artist["name"]} {artist["id"]}')
            print(self.ids[-1])
        
        while type(self.id) != int:
            try:
                self.id = int(input("Artist:\n"))
            except:
                print("Enter valid ID")
        
        return self.id



    def Search_choice(self) -> list:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
        search_type = None
        while search_type != int:
            try:    
                search_type = int(input("What kind of search?\n\n1. Search artist\n2. Searcg album\n3. Search track\n4. Search cover\n"))
                self.query = input("Query:\n")
            except:
                print("Please enter a valid number\n")
        
        if search_type == 1:
            self.Artist()
        
        if search_type == 2:
            self.Album()
        
        if search_type == 3:
            self.Track()
        
        if search_type == 4:
            self.Cover()
    
    def Choice(liste) -> list:
        print("\n")
        for item in len(liste):
            print(f"{item + 1}. {liste[item]}")