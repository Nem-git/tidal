import asyncio
import time
from ..tools.path import Path
from ..media.album import Album
from ..media.track import Track




class Order:
    async def Artist(self):
        pass

    async def Album(self, item_id : str, quality : str, path : str, artist_cover_path : str):
        
        resp = await Album().download_json(item_id=item_id)

        (
            item_id,
            title,
            track_number,
            date,
            year,
            copyrights,
            cover,
            explicit,
            artists,
            volume_number,
            tracks,
            #quality #Not sure if it's even useful, I'll have to check later
        ) = await Album().metadata(resp=resp)

        #queue = asyncio.Queue(0)
        
        album_cover_path = ""

        track_ids = []
        for track in tracks:
            track_id = track["item"]["id"]
            track_ids.append(track_id)


        for track_id in track_ids:
            print(track_id)
            await Order().Track(
                item_id=track_id,
                quality=quality,
                path=path,
                total_track_number=track_number,
                album_cover_path=album_cover_path,
                artist_cover_path=artist_cover_path
            )
        
        async_list = []

        #tasks = [asyncio.ensure_future(Order().Track(
        #    item_id=track_id,
        #    quality=quality,
        #    path=path,
        #    album_cover_path=album_cover_path,
        #    artist_cover_path=artist_cover_path
        #) for track_id in track_ids)]

        #await asyncio.gather(*tasks)




    async def Track(self, item_id: str, quality : str, path : str, total_track_number : str, album_cover_path : str, artist_cover_path : str):
        track = Track()
        

        resp : dict[str, str] = await track.download_json(item_id=item_id, quality=quality)

        (
            item_id,
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
            album
        ) = await track.metadata(track=resp, album={})

        path = "/".join((path, Path().Clean(string=artists), Path().Clean(string=album["title"])))
        Path().Create(path=path)
        
        track_path = f"{path}/{track_number} {Path().Clean(string=title)}{file_extension}"
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
            artist_cover_path=artist_cover_path
        )

ssss = time.time()
asyncio.run(main=Order().Album(item_id="201810799", quality="HI_RES_LOSSLESS", path=".", artist_cover_path=""))
print(time.time() - ssss)