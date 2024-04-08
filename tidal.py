import requests
import os


url = "https://host-hifi-restapi-on-vercel-git-main-sachinsenal0x64.vercel.app/"
url = "https://tidal.401658.xyz/"

def String_replace(old):
    old.replace("'", "")
    old.replace('"', "")
    old.replace("\\", "")
    return old

def Validate_request(request):
    response = requests.get(request)
    while response.status_code != 200:
        response = requests.get(request)
    return response.json()

def Download_song(song_id, song_quality, artist_name, release_year):
    song_response = Validate_request(f"{url}track/?id={song_id}&quality={song_quality}")
    song_path = f"../{artist_name}/{artist_name} - {song_response[0]['album']['title']} ({release_year})/"

    if not os.path.exists(String_replace(song_path)):
        os.makedirs(String_replace(song_path))
    else:
        "Something doesnt work with the path"
    
    with open(f"{song_path}{artist_name} - {song_response[0]['title']}.flac", "wb") as f:
        song_link = Validate_request(song_response[2]['OriginalTrackUrl'])
        f.write(song_link.content)
    Download_cover(song_response[0]['album']['cover'], song_path)


def Download_cover(cover_code, cover_path):
    if os.path.exists(f"{cover_path}cover.jpg"):
        return
    
    cover_url = "https://resources.tidal.com/images/"
    for i in cover_code.split("-"):
        cover_url += f"{i}/"

    with open(f"{cover_path}cover.jpg", "wb") as c:
        cover_response = Validate_request(f"{cover_url}640x640.jpg")
        c.write(cover_response.content)


os.system("cls")
while True:
    print("Download Artist ONLY(fuck you)\n")
    artist_name = String_replace(input("Artist Name: "))
    artist_response = Validate_request(f"{url}search/?a={artist_name}")

    for artist in artist_response[0]['artists']['items']:
        print(f"{artist['id']} - {artist['name']}")
    
    artist_id = input("Artist ID: ")
    os.system("cls")
    artist_id_response = Validate_request(f"{url}search/?f={artist_id}")

    for album in artist_id_response[1]:
        print(f"{album['id']}. {album['album']['title']} - {album['title']}")
        artist_name = artist_id_response[0]['rows'][0]['modules'][0]['pagedList']['items'][0]['artists'][0]['name']
        release_year = album['album']['releaseDate'].split("-")[0]
        Download_song(album['id'], "HI_RES_LOSSLESS", artist_name, release_year)
        
