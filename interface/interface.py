import asyncio

from tools import Order


class Interface:

    def __init__(self) -> None:
        print(
            """
Welcome to my TIDAL downloader!!
This program is only in alpha, but I 
hope to improve on it as time comes.
________________________________________________________
To select the different choices in the
menu below, you need to enter a number,
then press the ENTER/RETURN key.
________________________________________________________
Have fun!

Credits: A big thanks to 0x64 for making
this incredible reverse proxy and sacrificing
his account for the good of the community :)
https://github.com/sponsors/sachinsenal0x64
________________________________________________________

Here are the download options for now:

1. Search and Download a certain track
2. Search and Download an entire album
3. Search and Download an artist's whole discography
4. Search and Download the cover of an album
5. Search and Download a TIDAL playlist (WIP)
6. Download a song's lyrics (WIP)
________________________________________________________
"""
        )

        c = int(input("Choice: "))

        match c:

            case 1:
                self.Artist()

    def Artist(self) -> None:
        pass


main = Main()
