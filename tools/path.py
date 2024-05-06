import asyncio


class Path:

    def Clean(string):
        for c in '*?<>"|':
            string = string.replace(c, "")
        for c in "'\\/:":
            string = string.replace(c, "-")
        return string