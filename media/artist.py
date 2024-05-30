from .downloads import Download


class Artist:

    async def download_json(self, item_id: str) -> dict[str, str]:
        return await Download().Json(rq_type="artist", param={"f": item_id})

    async def metadata(self, resp: dict[str, str]) -> tuple[str]:

        name: str = resp[0]["artists"][0]["name"]
        album_number: int = len(resp)
        cover_id: str = resp[0]["artists"][0]["picture"]

        album_ids = []
        for album in resp:
            if album["album"]["id"] not in album_ids:
                album_ids.append(int(album["album"]["id"]))

        return (
            name,
            album_number,
            cover_id,
            album_ids,
        )

    async def search(self, query) -> list:
        resp = await Download().Search(rq_type="search", param={"a" : query})
        
        artists = []
        
        for artist in resp[0]["artists"]["items"]:
            artists.append([artist["id"], artist["name"]])
            
        print(artists)
        return artists