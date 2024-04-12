import requests
import os

class Song:
    artist_id = None
    artist_name = None
    album_id = None
    album_name = None
    track_id = None
    track_name = None
    track_number = None
    track_quality = None
    track_url = None

    def __init__(self) -> None:
        self.song_response = None






#song_response = requests.get(f"{url}track/?id={song_id}&quality={song_quality}").json()
#song_path = f"../{artist_name}/{artist_name} - {song_response[0]['album']['title']} ({release_year})/"

#if not os.path.exists(song_path):
#    os.makedirs(song_path)
#else:
#    "Something doesnt work with the path"
    
#with open(f"{song_path}{artist_name} - {song_response[0]['title']}.flac", "wb") as f:
#    song_link = requests.get(song_response[2]['OriginalTrackUrl'])
#    while 200 != song_link.status_code:
#        song_link = requests.get(song_response[2]['OriginalTrackUrl'])
#    f.write(song_link.content)
        


    def Download_track():




