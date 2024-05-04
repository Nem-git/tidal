from common import Common

download_url = "https://tidal.401658.xyz/album/"
id = 157117504
quality = "HI_RES_LOSSLESS"

response = Common.Send_request(download_url, {"id" : id})

a = response[0]
b = response[1]

response = a | b

#print(dictionnary)

artists = response.get("artists", [])
album_artists = ""
album_artists = " & ".join(artist["name"] for artist in artists)
print(album_artists)