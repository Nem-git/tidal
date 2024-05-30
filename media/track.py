import aiofiles
from mutagen import flac, mp4
from mutagen.id3 import PictureType
from .downloads import Download


class Track:

    async def download_media(self, path: str, url: str) -> None:
        await Download().Media(path=path, url=url, param={})

    async def download_json(self, item_id: str, quality: str) -> dict[str, str]:
        return await Download().Json(
            rq_type="track", param={"id": item_id, "quality": quality}
        )

    async def metadata(
        self, track: dict[str, str], album: dict[str, str]) -> tuple[str]:
        streamable: str | bool = track.get("allowStreaming", False)
        if not streamable:
            return

        title: str | None = track.get("title")
        track_number: str = f'{track.get("trackNumber", "1"):02}'
        volume_number: str = track.get("volumeNumber", "1")
        copyrights: str = track.get("copyright", "Not copyrighted")
        isrc: str = track.get("isrc", "")
        artists: str = " & ".join(artist["name"] for artist in track.get("artists"))

        version: str = track.get("version", "1")
        if track.get("version") is not None:
            title = f"{title} ({version})"

        qualities: dict[str, int] = {
            "LOW": 0,
            "HIGH": 1,
            "LOSSLESS": 2,
            "HI_RES": 3,
        }

        quality: int = qualities[track.get("audioQuality")]
        if quality >= 2:
            file_extension = ".flac"
        else:
            file_extension = ".m4a"

        url: str = track.get("OriginalTrackUrl")

        if album == {}:
            album = track.get("album")

        return (
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
        )

    async def tag(
        self,
        title: str,
        track_number: str,
        total_track_number: str,
        volume_number: str,
        copyrights: str,
        isrc: str,
        artists: str,
        file_extension: str,
        album: dict[str, str],
        track_path: str,
        album_cover_path: str,
        artist_cover_path: str,
    ) -> None:

        if file_extension == ".m4a":
            track = mp4.MP4(track_path)
            # track.add_tags()
            track.tags["\\xa9nam"] = title
            track.tags["\\xa9ART"] = artists
            track.tags["\\xa9alb"] = album.get("title")
            track.tags["cprt"] = copyrights
            # track.tags["----:com.apple.iTunes:ISRC"] = isrc.encode("utf-8")
            # #track.tags["trkn"] = str(object=track_number, ) #Need to add total_track_number
            # track.tags["disk"] = str(object=volume_number)

            if album_cover_path != "":
                async with aiofiles.open(file=album_cover_path, mode="rb") as c:
                    track["covr"] = mp4.MP4Cover(data=await c.read(), imageformat="FORMAT_JPEG")

        if file_extension == ".flac":
            track = flac.FLAC(track_path)
            track.add_tags()
            track.tags["TITLE"] = title
            track.tags["ARTIST"] = artists
            track.tags["ALBUM"] = album.get("title")
            track.tags["COPYRIGHT"] = copyrights
            # track.tags["ISRC"] = isrc.encode("utf-8")
            track.tags["TRACKNUMBER"] = str(object=track_number)
            track.tags["DISCNUMBER"] = str(object=volume_number)

        if artist_cover_path != "":
            async with aiofiles.open(file=artist_cover_path, mode="rb") as c:
                cover = flac.Picture()
                cover.data = await c.read()
                cover.type = PictureType.ARTIST
                cover.mime = "image/jpeg"
                cover.width = 1280
                cover.height = 1280
                track.add_picture(picture=cover)
        
        if album_cover_path != "":
            async with aiofiles.open(file=album_cover_path, mode="rb") as c:
                cover = flac.Picture()
                cover.data = await c.read()
                cover.type = PictureType.COVER_FRONT
                cover.mime = "image/jpeg"
                cover.width = 1280
                cover.height = 1280
                track.add_picture(picture=cover)

        track.save()

    async def search(self, query):# -> list[Any]:
        resp = await Download().Search(rq_type="search", param={"s" : query})
        
        tracks = []
        
        for track in resp["items"]:
            tracks.append([
                track["id"],
                track["title"],
                track["album"]["title"],
                track["artist"]["name"],
            ])
            
            
        print(tracks)
        return tracks