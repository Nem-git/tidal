import aiofiles
from mutagen import flac, mp4, id3
from .downloads import Download

class Track:

    async def download_media(path, url):
        await Download.Media(path, url, {})

    async def download_json(item_id, quality):
        return await Download.Json("track", {"id" : item_id, "quality" : quality})


    async def metadata(track, album):
        streamable = track.get("allowStreaming", False)
        if not streamable:
            return None

        item_id = track.get("id")
        title = track.get("title")
        track_number = f'{track.get("trackNumber", 1):02}'
        volume_number = track.get("volumeNumber", 1)
        copyrights = track.get("copyright", "Not copyrighted")
        isrc = track.get("isrc", "")
        artists = " & ".join(artist["name"] for artist in track.get("artists"))

        version = track.get("version", 1)
        if version is not None:
            title = (f"{title} ({version})")
        
        qualities = {
            "LOW": 0,
            "HIGH": 1,
            "LOSSLESS": 2,
            "HI_RES": 3,
        }

        quality = qualities[track.get("audioQuality")]
        if quality >= 2:
            file_extension = ".flac"
        else:
            file_extension = ".m4a"
        
        url = track.get("OriginalTrackUrl")

        if album is None:
            album = track.get("album")

        return (
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
            )
    

    async def tag(title, track_number, volume_number, copyrights, isrc, artists, file_extension, album, track_path, album_cover_path, artist_cover_path):
        
        if file_extension == ".m4a":
            track = mp4.MP4(track_path)
            track.add_tags()
            track.tags["\\xa9nam"] = title
            track.tags["\\xa9ART"] = artists
            track.tags["\\xa9alb"] = album.get("title")
            track.tags["cprt"] = copyrights
            #track.tags["----:com.apple.iTunes:ISRC"] = isrc.encode("utf-8")
            track.tags["trkn"] = str(track_number)
            track.tags["disk"] = str(volume_number)

            if album_cover_path is not None:
                async with aiofiles.open(album_cover_path, "rb") as c:
                    track["covr"] = mp4.MP4Cover(c.read(), imageformat=FORMAT_JPEG)


        if file_extension == ".flac":
            track = flac.FLAC(track_path)
            track.add_tags()
            track.tags["TITLE"] = title
            track.tags["ARTIST"] = artists
            track.tags["ALBUM"] = album.get("title")
            track.tags["COPYRIGHT"] = copyrights
            #track.tags["ISRC"] = isrc.encode("utf-8")
            track.tags["TRACKNUMBER"] = str(track_number)
            track.tags["DISCNUMBER"] = str(volume_number)

            if album_cover_path is not None:
                async with aiofiles.open(album_cover_path, "rb") as c:
                    cover = flac.Picture()
                    cover.data = c.read()
                    cover.type = id3.PictureType.COVER_FRONT
                    cover.mime = "image/jpeg"
                    cover.width = 1280
                    cover.height = 1280
                    track.add_picture(cover)
            
            if artist_cover_path is not None:
                async with aiofiles.open(artist_cover_path, "rb") as c:
                    cover = flac.Picture()
                    cover.data = c.read()
                    cover.type = id3.PictureType.ARTIST
                    cover.mime = "image/jpeg"
                    cover.width = 1280
                    cover.height = 1280
                    track.add_picture(cover)
        
        track.save()
            







            



