import aiohttp
import aiofiles


class Download:

    async def Media(self, path: str, url: str, param: dict[str, str]) -> None:
        """
        This Python async function downloads media content from a specified URL and saves it to a file at a
        given path.

        :param path: The `path` parameter in the `Media` function is a string that represents the file path
        where the downloaded media will be saved
        :type path: str
        :param url: The `url` parameter in the `Media` function is a string that represents the URL from
        which you want to download media content
        :type url: str
        :param param: The `param` parameter in the `Media` function is a dictionary that contains key-value
        pairs of parameters that will be sent in the HTTP request. These parameters are typically used for
        things like filtering, sorting, or specifying additional information for the request. In this case,
        the `param` dictionary is
        :type param: dict[str, str]
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, params=param) as resp:
                if resp.ok:
                    async with aiofiles.open(file=f"{path}", mode="wb") as track:
                        async for chunk in resp.content.iter_chunked(n=4096000):
                            await track.write(chunk)
                else:
                    print(f"Server gave back error {resp.status}")

    async def Json(
        self, rq_type: str, param: dict[str, str]
    ) -> dict[str, str] | dict[str, int]:
        """
        This Python async function sends a request to a Tidal API endpoint and processes the response based
        on the provided parameters.

        :param rq_type: The `rq_type` parameter in the provided code represents the type of request being
        made to the Tidal API. It is a string that specifies the category of data being requested, such as
        "artists", "albums", "videos", "items", or "playlists"
        :type rq_type: str
        :param param: The `param` parameter in the `Json` method is a dictionary that contains key-value
        pairs of parameters to be included in the request. These parameters are used to customize the
        request to the API endpoint specified by `rq_type`. The keys in the `param` dictionary correspond to
        different types of data
        :type param: dict[str, str]
        :return: The `Json` method returns a dictionary with string keys and string values. The specific
        content of the dictionary returned depends on the logic within the method and the input parameters
        provided.
        """

        types: dict[str, str] = {
            "a": "artists",
            "al": "albums",
            "v": "videos",
            "s": "items",
            "p": "playlists",
        }

        url: str = "/".join(("https://tidal.401658.xyz", rq_type))
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, params=param) as resp:
                if resp.status == 200:

                    for k in param.keys():
                        if k in types.keys():
                            s_type: dict[str, str] = await resp.json()

                            if k == "a":
                                s_type = await resp.json()
                                s_type = s_type[0]

                            s_type = s_type[types.get(k)]
                            return s_type

                    iter_dict: dict[str, str] = {}

                    if rq_type == "artist":
                        iter_dict = await resp.json()
                        iter_dict = iter_dict[0]["rows"][0]["modules"][0]["pagedList"][
                            "items"
                        ]

                    else:
                        for part in await resp.json():
                            if type(part) is list:
                                for j in part:
                                    iter_dict = iter_dict | j

                            else:
                                iter_dict = iter_dict | part

                    return iter_dict
