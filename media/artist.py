from .downloads import Download


class Album:
    
    async def download_json(self, item_id: str) -> dict[str, str]:
        return await Download().Json(rq_type="artist", param={"id": item_id})

    async def metadata(self, resp: dict[str, str]) -> tuple[str]:
        pass