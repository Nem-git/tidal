import asyncio
from aiohttp import ClientSession

async def download_file(url, file_name):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                file_size = int(resp.headers['Content-Length'])
                with open(file_name, 'wb') as fd:
                    progress = 0
                    while True:
                        chunk = await resp.content.read(1024)
                        if not chunk:
                            break
                        fd.write(chunk)
                        progress += len(chunk)
                        percentage = (progress / file_size) * 100
                        print(f"Download Progress: {percentage:.2f}%")
            else:
                print("Failed to download the file.")

#asyncio.run(download_file("https://sp-pr-cf.audio.tidal.com/mediatracks/CAEaKRInNjdmZGQ2ZWE1ODg3YzU0NDg4YmQ3MTZmNGQwM2QzYzRfNjEubXA0/0.flac?Expires=1715294274&Signature=wJ1oXA6LXk7aSjzz1T0oDPCMpINl0JTfGYcZhd2BhjworK2Up4~Gfg0PHqHf4Ko5m-B6MDS5uafZiri~CR~r8w26THz2SvRc4x0TebV2rTaxkZMCXcgbfnhaTiFuhKzzclJMRQYSyC8W177iexGy~7HyHLzHcBtLl3L2bC2WNYYnsY5rqlchL6foLjjC0-MvR6PMGUvC6w3PjhxKqItQ7NNiyGx0Jtxrg1Xa0JMWuq2puAslRPxVbOMyQByuwu444M-8o8-orL9d-0xmPkVCiwuMR0tYyurnt50HMvw0EVO6iB2UEAxUTtSfDeFiH1YVfq1udJgL-nbg5tL-or0zHw__&Key-Pair-Id=K14LZCZ9QUI4JL", "file.flac"))