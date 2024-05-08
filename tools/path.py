import os

class Path:

    def Clean(self, string : str) -> str:
        for c in '*?<>"|':
            string = string.replace(c, "")
        for c in "'\\/:":
            string = string.replace(c, " ")
        return string
    
    def Create(self, path : str) -> None:
        os.makedirs(name=path, exist_ok=True)