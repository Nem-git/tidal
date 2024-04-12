import requests
import os
from mutagen.flac import FLAC

url = "https://host-hifi-restapi-on-vercel-git-main-sachinsenal0x64.vercel.app/"
url = "https://tidal.401658.xyz/"

def Download_song(song_id, song_quality, artist_name, release_year):
    song_response = requests.get(f"{url}track/?id={song_id}&quality={song_quality}").json()
    song_path = f"../{artist_name}/{artist_name} - {song_response[0]['album']['title']} ({release_year})/"

    if not os.path.exists(song_path):
        os.makedirs(song_path)
    else:
        "Something doesnt work with the path"
    
    with open(f"{song_path}{artist_name} - {song_response[0]['title']}.flac", "wb") as f:
        song_link = requests.get(song_response[2]['OriginalTrackUrl'])
        while 200 != song_link.status_code:
            song_link = requests.get(song_response[2]['OriginalTrackUrl'])
        f.write(song_link.content)
    Download_cover(song_response[0]['album']['cover'], song_path)


def Download_cover(cover_code, cover_path):
    if os.path.exists(f"{cover_path}cover.jpg"):
        return
    
    cover_url = "https://resources.tidal.com/images/"
    for i in cover_code.split("-"):
        cover_url += f"{i}/"

    with open(f"{cover_path}cover.jpg", "wb") as c:
        cover_response = requests.get(f"{cover_url}640x640.jpg")
        while 200 != cover_response.status_code:
            cover_response = requests.get(f"{cover_url}640x640.jpg")
        c.write(cover_response.content)


f = FLAC(f"../Annie Brocoli/Annie Brocoli/04 Ma coccinelle.flac")
print(f.tags)



#os.system("clear")
#while True:
#    print("Download Artist ONLY(fuck you)\n")
#    artist_name = input("Artist Name: ")
#    artist_response = requests.get(f"{url}search/?a={artist_name}").json()
#
#    for artist in artist_response[0]['artists']['items']:
#        print(f"{artist['id']} - {artist['name']}")
#    
#    artist_id = input("Artist ID: ")
#    os.system("clear")
#    artist_id_response = requests.get(f"{url}search/?f={artist_id}").json()
#
#    for album in artist_id_response[1]:
#        print(f"{album['id']}. {album['album']['title']} - {album['title']}")
#        artist_name = artist_id_response[0]['rows'][0]['modules'][0]['pagedList']['items'][0]['artists'][0]['name']
#        release_year = album['album']['releaseDate'].split("-")[0]
#        Download_song(album['id'], "HI_RES_LOSSLESS", artist_name, release_year)
        
