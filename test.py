import requests
import json
from simple_term_menu import TerminalMenu

url = "https://host-hifi-restapi-on-vercel-git-main-sachinsenal0x64.vercel.app/"


query = "Starships"
def preview_content():
    return f"{liste[song]['title']}"

querystring = {"q":query}
response = 0
while type(response) != list:
    try:
        response = requests.get(f"{url}search/", params=querystring).json()
    except:
        pass

liste = []
for part in range(len(response)):
    joined = {}
    joined.update(response[part])
    liste.append(joined)

summary = []

for song in range(len(liste)):
    summary.append(f"{song + 1}. {liste[song]['title']} by {liste[song]['artist']['name']} [{liste[song]['id']}]")

terminal_menu = TerminalMenu(
    summary,
    title=(f"Results for track '{query}' from Tidal\nSPACE - select, ENTER - download, ESC - exit"),
    preview_command="bat --color=always code/tidal.py",
    preview_size=0.75,
    cycle_cursor=True,
    clear_screen=True,
    multi_select=True,
    multi_select_select_on_accept=False,
)

chosen = terminal_menu.show()
#if chosen is None:
#    print("Nothing chosen, exiting..")
#else:
#    for song in range(chosen):
#        with open(f"{liste[song]['artist']['name']} - {liste[song]['title']}.flac", "wb") as f:
#            f.write(requests.get(id_quality_song(liste[song]["id"], "HI_RES_LOSSLESS").content))



#print(response)
#print("\n\n\n\n", joined)
#print(joined["OriginalTrackUrl"])
#print(requests.get(joined["OriginalTrackUrl"]))

#with open("file.flac", "wb") as f:
#    f.write(requests.get(joined["OriginalTrackUrl"]).content)