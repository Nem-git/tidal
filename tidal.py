import requests
import pandas as pd
import json
import os

url = "https://tidal.401658.xyz"
url = "https://host-hifi-restapi-on-vercel-git-main-sachinsenal0x64.vercel.app"
qualities = ["HI_RES_LOSSLESS", "HI_RES", "LOSSLESS", "HIGH", "LOW"]

def query_song(query):
    querystring = {"q":query}
    response = 0
    while type(response) != list:
        try:
            response = requests.get(f"{url}/search/", params=querystring).json()
        except:
            pass

    joined = {}
    for parts in response:
        joined.update(parts)
    

def query_quality_song(query, quality):
    querystring = {"q":query, "quality":quality}
    response = 0
    while type(response) != list:
        try:
            response = requests.get(f"{url}/song/", params=querystring).json()
        except:
            pass
    
    joined = {}
    for parts in response:
        joined.update(parts)
    print(joined["OriginalTrackUrl"])

def id_quality_song(id, quality):
    querystring = {"id":id, "quality":quality}
    response = 0
    while type(response) != list:
        try:
            response = requests.get(f"{url}/track/", params=querystring).json()
        except:
            pass
    
    joined = {}
    for parts in response:
        joined.update(parts)
    print(joined["OriginalTrackUrl"])


while True:
    search_download = int(input("1. Search for song\n2. Download anything\n\n"))
    os.system("clear")
    
    if search_download == 1:
        search_option = int(input("1. Query song(no quality)\n2. Query song(needs quality)\n3. ID song(needs quality)\n\n"))
        os.system("clear")
        if search_option == 1:
            query_song(input("Query: "))
            os.system("clear")
        
        else:
            quality_choice = int(input(f"1. {qualities[0]}\n2. {qualities[1]}\n3. {qualities[2]}\n4. {qualities[3]}\n5. {qualities[4]}\n\n"))
            os.system("clear")
            quality = qualities[quality_choice - 1]

            if search_option == 2:
                query_quality_song(input("Query: "), quality)
            
            if search_option == 3:
                id_quality_song(int(input("ID: "), quality))
            


    if search_download == 2:
        None
    
        if search_download[1] == 1:
            None
        
        if search_download[1] == 2:
            None

        if search_download[1] == 3:
            None
        
        if search_download[1] == 4:
            None

        if search_download[1] == 5:
            None
