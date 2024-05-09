from .downloads import Download

class Album:

    async def download_json(self, item_id: str) -> dict[str, str]:
        return await Download().Json(rq_type="album", param={"id": item_id})

    async def metadata(self, resp: dict[str, str]) -> tuple[str]:
        streamable: str | bool = resp.get("allowStreaming", False)
        if not streamable:
            return

        title: str = resp.get("title", "Unknown Album")
        track_number: str | None = resp.get("numberOfTracks")
        date: str | None = resp.get("releaseDate")
        year: str = date[:4]
        copyrights: str = resp.get("copyright", "Not copyrighted")
        explicit: str | bool = resp.get("explicit", False)
        artists: str = " & ".join(artist["name"] for artist in resp.get("artists", []))
        volume_number: str | None = resp.get("numberOfVolumes")

        qualities: dict[str, int] = {
            "LOW": 0,
            "HIGH": 1,
            "LOSSLESS": 2,
            "HI_RES": 3,
        }

        quality: int = qualities[resp.get("audioQuality")]

        tracks: str | None = resp.get("items")

        cover_id = None  # Temporary

        return (
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
        )  # , quality
