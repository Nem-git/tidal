# How to use the Tidal Music Downloader:

### Cloning the repository
```
git clone https://github.com/Nem-git/tidal.git
```

### Installing the dependencies
```
cd tidal/
pip -r requirements.txt
```

## Arguments
```
search
download
artist
album
track
cover
```

## Examples

### Searching for an artist
```
python tidal/main.py search artist "Dua Lipa"
```

### Searching for a track
```
python tidal/main.py search track "Not like us"
```

### Downloading an artist's entire discography
```
python tidal/main.py download artist 9127
```

### Downloading an entire album
```
python tidal/main.py download track 364531268
```

### Downloading an album cover
```
python tidal/main.py download cover "899da3f4-54bb-4b2d-bed3-06da2c503075"
```

## Dependencies

**Hifi-Tui Docs**
https://tidal.401658.xyz/tdoc
https://github.com/sachinsenal0x64/HIFI-TUI?tab=readme-ov-file#-api-documentation

**Hifi-Tui API**
https://tidal.401658.xyz/

**Mutagen Docs**
https://mutagen.readthedocs.io/en/latest/api/id3.html
