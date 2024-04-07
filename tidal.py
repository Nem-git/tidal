import requests
import os


url = "https://host-hifi-restapi-on-vercel-git-main-sachinsenal0x64.vercel.app/"
url = "https://tidal.401658.xyz/"

def Download_song(song_id, song_quality, artist_name, release_year):
    song_response = requests.get(f"{url}track/?id={song_id}&quality={song_quality}").json()

    song_path = f"../{artist_name}/{artist_name} - {song_response[0]['album']['title']}"

    if not os.path.exists(song_path):
        os.makedirs(song_path)
    else:
        "Something doesnt work with the path"
    
    with open(f"{song_path}/{artist_name} - {song_response[0]['title']}.flac", "wb") as f:
        req = requests.get(song_response[2]['OriginalTrackUrl']).content
        while "Error" in str(req):
            req = requests.get(song_response[2]['OriginalTrackUrl']).content
        f.write(req)

def Download_cover(song_response):



os.system("clear")
while True:
    print("Download Artist ONLY(fuck you)\n")
    artist_name = input("Artist Name: ")
    artist_response = requests.get(f"{url}search/?a={artist_name}").json()

    for artist in artist_response[0]['artists']['items']:
        print(f"{artist['id']} - {artist['name']}")
    
    artist_id = input("Artist ID: ")
    os.system("clear")
    artist_id_response = requests.get(f"{url}search/?f={artist_id}").json()

    for album in artist_id_response[1]:
        print(f"{album['id']}. {album['album']['title']} - {album['title']}")
        song_response = requests.get(f"{url}track/?id={album['id']}&quality=HI_RES_LOSSLESS").json()
        Download_song(album['id'], "HI_RES_LOSSLESS", artist_id_response[0]['rows'][0]['modules'][0]['pagedList']['items'][0]['artists'][0]['name'])
