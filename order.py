import asyncio
import tqdm
import time
from tools.path import Path
from media.artist import Artist
from media.album import Album
from media.track import Track
from media.cover import Cover


class Order:
    async def Artist(
        self, item_id : str, quality : str, path:str
    ) -> None:
        
        artist = Artist()
        
        resp: dict[str, str] = await artist.download_json(item_id=item_id)
        
        (
            name,
            album_number,
            cover_id,
            album_ids,
        ) = await artist.metadata(resp=resp)
        
        if cover_id:
            artist_cover_path: str = f"{path}{name}/artist.jpg"
            await self.Cover(id=cover_id, resolution=1280, path=artist_cover_path)
        
        
        # Async
#        async with asyncio.TaskGroup() as tg:
#            for album_id in album_ids:
#                tg.create_task(
#                    coro=Order().Album(
#                        item_id=album_id,
#                        quality=quality,
#                        path=path,
#                        artist_cover_path=artist_cover_path
#                    )
#                )

        # Not async
        for album_id in album_ids:
            await Order().Album(item_id=album_id,quality=quality,path=path, artist_cover_path=artist_cover_path)


    async def Album(self, item_id: str, quality: str, path: str, artist_cover_path: str) -> None:
        
        album = Album()
        
        resp: dict[str, str] = await album.download_json(item_id=item_id)
        
        try:
            if resp["status"] == 404:
                print(resp["userMessage"])
                return
        except:
            pass
        
        (
            title,
            track_number,
            date,
            year,
            copyrights,
            cover_id,
            explicit,
            artists,
            volume_number,
            tracks,
        ) = await album.metadata(resp=resp)

        album_cover_path: str = "" #Just for now
        
        if cover_id:
            album_cover_path: str = f"{path}/cover.jpg"
            await self.Cover(id=cover_id, resolution=1280, path=album_cover_path)

        track_ids: list[str] = []
        for track in tracks:
            track_id: str = track["item"]["id"]
            track_ids.append(track_id)

# Async
#        async with asyncio.TaskGroup() as tg:
#            for track_id in tqdm.tqdm(iterable=track_ids,
#                            desc=f"{title} ({year})",
#                            unit=" track",
#                            ascii=False):
#                tg.create_task(
#                    coro=Order().Track(
#                        item_id=track_id,
#                        quality=quality,
#                        path=path,
#                        total_track_number=track_number,
#                        album_cover_path=album_cover_path,
#                        artist_cover_path=artist_cover_path,
#                    )
#                )

# Not async
        for track_id in tqdm.tqdm(iterable=track_ids,
                        desc=f"{title} ({year})",
                        unit=" track",
                        ascii=False):
            await Order().Track(
                item_id=track_id,
                quality=quality,
                path=path,
                total_track_number=track_number,
                album_cover_path=album_cover_path,
                artist_cover_path=artist_cover_path,
            )


    async def Track(
        self,
        item_id: str,
        quality: str,
        path: str,
        total_track_number: str,
        album_cover_path: str,
        artist_cover_path: str,
    ) -> None:
        
        track = Track()
        
        resp: dict[str, str] = await track.download_json(
            item_id=item_id, quality=quality
        )

        (
            title,
            track_number,
            volume_number,
            copyrights,
            isrc,
            artists,
            version,
            quality,
            file_extension,
            url,
            album,
        ) = await track.metadata(track=resp, album={})

        path = "/".join(
            (path, Path().Clean(string=artists), Path().Clean(string=album["title"]))
        )

        Path().Create(path=path)

        track_path: str = (
            f"{path}/{track_number} {Path().Clean(string=title)}{file_extension}"
        )
        
        await track.download_media(path=track_path, url=url)
        

        await track.tag(
            title=title,
            track_number=track_number,
            total_track_number=total_track_number,
            volume_number=volume_number,
            copyrights=copyrights,
            isrc=isrc,
            artists=artists,
            file_extension=file_extension,
            album=album,
            track_path=track_path,
            album_cover_path=album_cover_path,
            artist_cover_path=artist_cover_path,
        )

    async def Cover(self, id: str, resolution: int, path: str) -> None:
        
        cover = Cover()
        
        url: str = f"https://resources.tidal.com/images/{id.replace("-", "/")}/{resolution}x{resolution}.jpg"
        
        await cover.download_media(path=path, url=url)
        


# Les Cowboys Fringants 4907832
# NWA 9127
# Michael Jackson 606
# Linkin Park 14123

if __name__ == "__main__":
    ssss: float = time.time()
    order = Order()
    
    # Download Artist
    #asyncio.run(main=order.Artist(item_id="9127", quality="HI_RES_LOSSLESS", path="../"))
    
    # Download Album
    #asyncio.run(main=order.Album(item_id="606", quality="HI_RES_LOSSLESS", path="../"))
    
    # Download Track
    #asyncio.run(main=order.Track(item_id="77686338", quality="HI_RES_LOSSLESS", path="../", total_track_number="14", album_cover_path="", artist_cover_path=""))
    
    # Download Cover
    #asyncio.run(main=order.Cover(id="84299843-40fe-487f-ad7d-35ecadb6e37c", resolution=750, path="../cover.jpg"))
    
    # Search Cover
    #asyncio.run(main=Cover().search(query="NWA"))
    
    # Search Artist
    #asyncio.run(main=Artist().search(query="NWA"))

    # Search Album
    #asyncio.run(main=Album().search(query="NWA"))
    
    # Search Track
    #asyncio.run(main=Track().search(query="Consequence"))
    
    print(time.time() - ssss)
