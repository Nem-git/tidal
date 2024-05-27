import tkinter as tk
from tkinter import ttk

class Interface:
    root = tk.Tk()
    
    def Choice(self) -> None:
        
        window = ttk.Frame(master=self.root).pack(fill="x", expand=True)
        self.root.title(string="Tidal Music Downloader")
        
        tk.Label(master=window, text="Tidal Music Downloader\nPlease select the type of content you'd like to download").pack(fill="x", expand=True)
        
        tk.Button(master=window, text="Artist", command=lambda: self.Artist()).pack(fill="x", expand=True)
        tk.Button(master=window, text="Album").pack(fill="x", expand=True)
        tk.Button(master=window, text="Track").pack(fill="x", expand=True)
        
        self.root.mainloop()
    
    def Artist(self) -> None:
        
        window = ttk.Frame(master=self.root).pack(fill="x", expand=True)
        self.root.title(string="Artist")
        
        tk.Label(master=window, text="Tidal Music Downloader\nPlease enter the artist name's discography you'd like to download").pack(fill="x", expand=True)
        artist = tk.StringVar()
        textbox = tk.Entry(master=window, textvariable=artist).pack(fill="x", expand=True)
        tk.Button(master=window, text="Search", command=lambda: self.Returning(something=artist.get())).pack(fill="x", expand=True)
        

    def Returning(self, something: str, window) -> str:
        print(something)
        window.quit()
        return something


interface = Interface()

main: None=interface.Choice()