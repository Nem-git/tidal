import requests
from common import Common

response = Common.Send_request("https://tidal.401658.xyz/track/", {"id" : 52438080, "quality" : "HI_RES_LOSSLESS"})
url = response[2]["OriginalTrackUrl"]
#url = "https://ab-pr-cf.audio.tidal.com/08083425/3308d4c10eb7dfb1b527a902cd7d1abd_37.m4a?Expires=1714008812&Signature=M-OXVbddBM1toxKQm-AwuWe5sxnVZ5QoHjj-V4q4BOsEgcDLlOQ6uCLrAl4H~ct3emZiGhXS88etA0w34dBNUEnK9-1nahHhOtMubCQh3FYtXa1EQiau41BXwPJSBypOvM47JVYBoFpPs~a3Tl2yHU3-5wgBAOydbs1DCrrim0W-aFMNVKcNwBnSykM3uUM4sGOR1IE7A-d5GIKvGBC8tHsgCayqgatUCQGZsoi1g-YA3ZgWmGvbZoj1sCuHkr1s-McMiY1A6qHJBkqezS0AQUi-00hf0EldKCKrXuVpW9PAHijacrcHj8GBUKl3QPp2Hg--4Fp48v8a28XuNYNNBg__&Key-Pair-Id=K14LZCZ9QUI4JL"

#url = url.split(".")[4].split("?")[0]
#print(url)




with open(f'test.{url.split(".")[4].split("?")[0]}', "wb") as track:
    resp = requests.get(url)
    while resp.status_code != 200:
        resp = requests.get(url)
    track.write(resp.content)
