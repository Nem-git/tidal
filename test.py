import asyncio
from media.downloads import Download
from time import time

async def down(item_id: int) -> dict[str, str]:
    b = await Download().Json(rq_type="artist", param={"id": item_id})
    c = await Download().Json(rq_type="artist", param={"f": item_id})

    with open(f"../{time()}.json", "w") as f:
        f.write(str(b))
    
    with open(f"../{time()}.json", "w") as f:
        f.write(str(c))
    


a = asyncio.run(down(9127))

print(a)