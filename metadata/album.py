from .cover import Cover


class AlbumMetadata:
    def collect(response):
        streamable = response.get("allowStreaming", False)
        if not streamable:
            return None
        
        id = response.get("id")
        album = response.get("title", "Unknown Album")
        track_number = response.get("numberOfTracks")
        date = response.get("releaseDate")
        year = date[:4]
        copyrights = response.get("copyright", "Not copyrighted")
        cover = Cover.collect(response)
        explicit = response.get("explicit", False)
        artists = response.get("artists", [])
        album_artists = " & ".join(artist["name"] for artist in artists)
        volume_number = response.get("numberOfVolumes")

        return 



        