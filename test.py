import requests
from common import Common

response = Common.Send_request("https://tidal.401658.xyz/artist/", {"id" : 4907832})
if response[1][0]["750"] is not None:
    cover = response[1][0]["750"]

with open(f'../cover.jpg', "wb") as c:
    response = requests.get(cover)
    while response.status_code != 200:
        response = requests.get(cover)
    c.write(response.content)

