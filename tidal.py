import requests
import os
import json


url = "https://host-hifi-restapi-on-vercel-git-main-sachinsenal0x64.vercel.app/"
url = "https://tidal.401658.xyz/"

def Download_song(song_response):
    with open(f"{artist['name']} - {song['name']}.flac", "wb") as f:
        f.write(requests.get(song_response[2]['OriginalTrackUrl']).content)



os.system("clear")
while True:
    print("Download Artist ONLY(fuck you)\n")
    artist_name = input("Artist Name: ")
    artist_response = 0
    while type(artist_response) != list:
        try:
            artist_response = requests.get(f"{url}search/?a={artist_name}").json()
        except:
            pass
    artist_joined = {}

    for parts in artist_response:
        artist_joined.update(parts)
    
    for artist in artist_joined['artists']['items']:
        print(f"{artist['id']} - {artist['name']}")
    
    artist_id = input("Artist ID: ")
    os.system("clear")
    artist_id_response = 0
    while type(artist_id_response) != list:
        try:
            artist_id_response = requests.get(f"{url}search/?f={artist_id}").json()
        except:
            pass

    for album in artist_id_response[1]:
        #print(f"{album['id']} - {album['title']}")
        album_response = 0
        while type(album_response) != list:
            try:
                album_response = requests.get(f"{url}album/?id={album['album']['id']}").json()
                print(f"{album_response[0]['artist']['name']} - {album_response[0]['title']}")
                song_response = 0
                nb = 0
                while type(song_response) != list:
                    try:
                        while nb < album_response[0]['numberOfTracks']:
                            print(album_response[1]['items'][nb]['item']['id'])
                            song_response = requests.get(f"{url}track/?id={album_response[1]['items'][nb]['item']['id']}&quality=HI_RES_LOSSLESS").json()
                            Download_song(song_response)
                            nb += 1

                    except:
                        pass
            except:
                pass
            
            
        


        




#        with open(f"{artist['name']} - {song['name']}.flac", "wb") as f:
#            f.write(requests.get(song["OriginalTrackUrl"]).content)
