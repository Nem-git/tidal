import asyncio
from .downloads import Download


class Album:

    async def download_json(item_id):
        return await Download.Json("album", {"id" : item_id})
    

    async def metadata(resp):
        streamable = resp.get("allowStreaming", False)
        if not streamable:
            return None
        
        item_id = resp.get("id")
        title = resp.get("title", "Unknown Album")
        track_number = resp.get("numberOfTracks")
        date = resp.get("releaseDate")
        year = date[:4]
        copyrights = resp.get("copyright", "Not copyrighted")
        explicit = resp.get("explicit", False)
        artists = " & ".join(artist["name"] for artist in resp.get("artists", []))
        volume_number = resp.get("numberOfVolumes")

        qualities = {
            "LOW": 0,
            "HIGH": 1,
            "LOSSLESS": 2,
            "HI_RES": 3,
        }

        quality = qualities[resp.get("audioQuality")]

        return item_id, title, track_number, date, year, copyrights, cover, explicit, artists, volume_number#, quality




    