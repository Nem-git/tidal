import asyncio
from media.downloads import Download
from time import time

async def down(item_id: int) -> None:
    #b = Download().Json(rq_type="artist", param={"id": item_id})
    c = Download().Json(rq_type="artist", param={"f": item_id})

    #with open(f"../{time()}.json", "w") as f:
    #    f.write(str(await b))
    
    with open(f"../{time()}.json", "w") as f:
        f.write(str(await c))
    


a = asyncio.run(down(9127))

print(a)