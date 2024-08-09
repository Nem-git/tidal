from . import Download

class Cover:
    
    async def download_media(self, path: str, url: str) -> None:
        await Download().Media(path=path, url=url, param={})
    
    async def search(self, query) -> list:
        resp = await Download().Search(rq_type="cover", param={"q" : query})
        
        covers = []
        for cover in resp:
            covers.append([cover["id"], cover["name"], cover["1280"]])
        
        print(covers)
        return covers