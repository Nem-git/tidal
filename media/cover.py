import aiofiles
from .downloads import Download

class Cover:
    
    async def download_media(self, path: str, url: str) -> None:
        await Download().Media(path=path, url=url, param={})