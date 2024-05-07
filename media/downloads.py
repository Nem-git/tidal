import aiohttp
import aiofiles

class Download:

    async def Media(path, url, param):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=param) as resp:
                if resp.ok:
                    async with aiofiles.open(f"{path}", "wb") as track:
                        async for chunk in resp.content.iter_chunked(4096000):
                            await track.write(chunk)
                else:
                    print(f"Server gave back error {resp.status}")

    async def Json(rq_type, param):
        
        types = {
        "a" : "artists",
        "al" : "albums",
        "v" : "videos",
        "s" : "items",
        "p" : "playlists"
        }

        url = "/".join(("https://tidal.401658.xyz", rq_type))
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=param) as resp:
                if resp.status == 200 and resp.status != 404:
                    for p in param.keys():
                        if p in types.keys():
                            s_type = await resp.json()

                            if p == "a":
                                s_type = await resp.json()
                                s_type = s_type[0]
                            
                            s_type = s_type[types.get(p)]
                            return s_type

                    new = {}
                    for i in await resp.json():
                        if type(i) is list:
                            for j in i:
                                new = new | j

                        else:
                            new = new | i
                    return new