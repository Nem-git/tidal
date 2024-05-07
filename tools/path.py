import os

class Path:

    def Clean(string):
        for c in '*?<>"|':
            string = string.replace(c, "")
        for c in "'\\/:":
            string = string.replace(c, "-")
        return string
    
    def Create(path):
        os.makedirs(path, exist_ok=True)