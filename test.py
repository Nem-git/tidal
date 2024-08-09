import tkinter as tk
from tkinter import Toplevel, ttk
import asyncio
from media.artist import Artist


class Interface:

    def Main(self) -> None:
        master = tk.Tk()
        window = ttk.Frame(master=master).grid(row=0, column=0)
        master.title(string="Tidal Music Downloader")

        tk.Label(
            master=window,
            text="Tidal Music Downloader\nPlease select the type of content you'd like to download",
        ).grid(row=1, column=0)

        tk.Button(
            master=window,
            text="Artist",
            command=lambda: self.Artist(master=master),
        ).grid(row=2, column=0)

        tk.Button(
            master=window,
            text="Album",
            command=lambda: self.Album(master=master),
        ).grid(row=3, column=0)

        tk.Button(
            master=window,
            text="Track",
            command=lambda: self.Track(master=master),
        ).grid(row=4, column=0)

        master.mainloop()

    def Artist(self, master: tk.Tk) -> None:

        window = Toplevel(master=master)
        window.title(string="Artist")

        tk.Label(
            master=window,
            text="Tidal Music Downloader\nPlease enter the name of the artist whose entire discography you want to download",
        ).grid(row=1, column=0)

        artist_var = tk.StringVar()

        tk.Entry(master=window, textvariable=artist_var).grid(row=2, column=0)

        tk.Button(
            master=window,
            text="Search",
            command=lambda: ArtistUI().Call_Function(
                command=Artist().search(query=artist_var.get()),
                window=window,
            ),
        ).grid(row=3, column=0)


interface = Interface()

asyncio.run(main=interface.Main())
