import requests
import os
from pick import pick
from simple_term_menu import TerminalMenu


url = "https://host-hifi-restapi-on-vercel-git-main-sachinsenal0x64.vercel.app"
url = "https://tidal.401658.xyz"
qualities = ["HI_RES_LOSSLESS", "HI_RES", "LOSSLESS", "HIGH", "LOW"]

def query_song(query):

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

    print(summary)

    #if os.name == "nt":
    #    from pick import pick
    #
    #    choices = pick(
    #        summary,
    #        title=(
    #            f"Results for track '{query}' from Tidal\nSPACE - select, ENTER - download, ESC - exit"
    #        ),
    #        min_selection_count=1,
    #        multiselect=True,
    #    )
    #
    #    choices()
    #    print(choices)


    title = 'Please choose your favorite programming language (press SPACE to mark, ENTER to continue): '
    options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
    option, index = pick(options, title)
    print(option)
    print(index)
    print("\n\n\n")






    #terminal_menu = TerminalMenu(
    #    summary,
    #    title=(f"Results for track '{query}' from Tidal\nSPACE - select, ENTER - download, ESC - exit"),
    #    preview_command="bat --color=always code/tidal.py",
    #    preview_size=0.75,
    #    cycle_cursor=True,
    #    clear_screen=True,
    #    multi_select=True,
    #    multi_select_select_on_accept=False,
    #)
    #
    #chosen = terminal_menu.show()


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
    

def query_quality_song(query, quality):
    querystring = {"q":query, "quality":quality}
    response = 0
    while type(response) != list:
        try:
            response = requests.get(f"{url}/song/", params=querystring).json()
        except:
            pass
    
    joined = {}
    for parts in response:
        joined.update(parts)
    print(joined["OriginalTrackUrl"])

def id_quality_song(id, quality):
    querystring = {"id":id, "quality":quality}
    response = 0
    while type(response) != list:
        try:
            response = requests.get(f"{url}/track/", params=querystring).json()
        except:
            pass
    
    joined = {}
    for parts in response:
        joined.update(parts)
    print(joined["OriginalTrackUrl"])


while True:
    search_download = int(input("1. Search for song\n2. Download anything\n\n"))
    os.system("clear")
    
    if search_download == 1:
        search_option = int(input("1. Query song(no quality)\n2. Query song(needs quality)\n3. ID song(needs quality)\n\n"))
        os.system("clear")
        if search_option == 1:
            query_song(input("Query: "))
            os.system("clear")
        
        else:
            quality_choice = int(input(f"1. {qualities[0]}\n2. {qualities[1]}\n3. {qualities[2]}\n4. {qualities[3]}\n5. {qualities[4]}\n\n"))
            os.system("clear")
            quality = qualities[quality_choice - 1]

            if search_option == 2:
                query_quality_song(input("Query: "), quality)
            
            if search_option == 3:
                id_quality_song(int(input("ID: "), quality))
            


    if search_download == 2:
        None
    
        if search_download[1] == 1:
            None
        
        if search_download[1] == 2:
            None

        if search_download[1] == 3:
            None
        
        if search_download[1] == 4:
            None

        if search_download[1] == 5:
            None
