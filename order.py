import asyncio
import tqdm
import time
from tools.path import Path
from media.artist import Artist
from media.album import Album
from media.track import Track


class Order:
    async def Artist(
        self, item_id : str, quality : str, path:str
    ) -> None:
        
        try:
            resp: dict[str, str] = await Artist().download_json(item_id=item_id)
        except:
            print(f"Error while trying to get json from {item_id}")
        
        try:
            (
                name,
                album_number,
                cover_id,
                album_ids,
            ) = await Artist().metadata(resp=resp)
        except:
            print(f"Error while trying to get metadata from {name}")
        
        artist_cover_path: str = ""
        
        sem = asyncio.Semaphore(value=1)
        
        print(name)
        async with asyncio.TaskGroup() as tg:
            for album_id in album_ids:
                async with sem:
                    tg.create_task(
                        coro=Order().Album(
                            item_id=album_id,
                            quality=quality,
                            path=path,
                            artist_cover_path=artist_cover_path
                        )
                    )
         

    async def Album(
        self, item_id: str, quality: str, path: str, artist_cover_path: str
    ) -> None:
        
        try:
            resp: dict[str, str] = await Album().download_json(item_id=item_id)
        except:
            print(f"Error while trying to download json from {item_id}")
        
        try:
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
            ) = await Album().metadata(resp=resp)
        except:
            print(f"Error while trying to get metadata from {title}")

        album_cover_path: str = ""

        track_ids: list[str] = []
        for track in tracks:
            track_id: str = track["item"]["id"]
            track_ids.append(track_id)
            
        sem = asyncio.Semaphore(value=3)

        async with asyncio.TaskGroup() as tg:
            for track_id in tqdm.tqdm(iterable=track_ids,
                            desc=f"{title} ({year})",
                            unit=" track",
                            ascii=False):
                async with sem:
                    tg.create_task(
                        coro=Order().Track(
                            item_id=track_id,
                            quality=quality,
                            path=path,
                            total_track_number=track_number,
                            album_cover_path=album_cover_path,
                            artist_cover_path=artist_cover_path,
                        )
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

        try:
            resp: dict[str, str] = await track.download_json(
                item_id=item_id, quality=quality
            )
        except:
            print(f"Error while trying to download json from {item_id}")

        try:
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
        except:
            print(f"Error while trying to get metadata from {title}")

        path = "/".join(
            (path, Path().Clean(string=artists), Path().Clean(string=album["title"]))
        )

        Path().Create(path=path)

        track_path: str = (
            f"{path}/{track_number} {Path().Clean(string=title)}{file_extension}"
        )
        
        try:
            await track.download_media(path=track_path, url=url)
        except:
            print(f"Error while trying to download media {title}")
        
        #print(f"{track_number} - {title}")

        try:
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
        except:
            print(f"Error while trying to tag {title}")


ssss: float = time.time()
# Les Cowboys Fringants 4907832
# NWA 9127
# Michael Jackson 606
asyncio.run(
    main=Order().Artist(
        item_id="606", quality="HI_RES_LOSSLESS", path="../"
    )
)
print(time.time() - ssss)
