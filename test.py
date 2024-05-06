import asyncio
from media.downloads import Download


a = asyncio.run(Download.Json("album", {"id" : 49820183}))

print(a)