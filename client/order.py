import asyncio
import time
from ..tools.path import Path
from ..media.album import Album
from ..media.track import Track




class Order:
    async def Artist():
        pass

    async def Album(album_cover_path, artist_cover_path):
        pass


    async def Track(item_id, quality, path, album_cover_path, artist_cover_path):
        ssss = time.time()

        resp = await Track.download_json(item_id, quality)
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
        ) = await Track.metadata(resp, None)

        path = "/".join((path, Path.Clean(artists), Path.Clean(album["title"])))
        Track.create_dir(path)
        
        track_path = f"{path}/{track_number} {Path.Clean(title)}{file_extension}"
        await Track.download_media(track_path, url)

        await Track.tag(
            title,
            track_number,
            volume_number,
            copyrights,
            isrc,
            artists,
            file_extension,
            album,
            track_path,
            album_cover_path,
            artist_cover_path
        )

        print(time.time() - ssss)


asyncio.run(Order.Track(49820191, "HI_RES_LOSSLESS", ".", None, None))