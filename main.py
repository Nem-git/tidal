from song import Song
from cover import Cover

song = Song()
cover = Cover()




song.id = "173889386"
song.quality = "HI_RES_LOSSLESS"



song.Infos()
song.Download()
cover.id = song.id
cover.path = song.path
cover.Download()



song.Tag()
