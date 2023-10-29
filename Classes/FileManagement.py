import os
import json

class FileManagement:
    def __init__(self, path):
        self.path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        if not os.path.isdir("Files/FileManagement"):
            raise ValueError("Path is not valid")
        self.__path = value

    def __writeJson(self,inputValue):
        with open(self.path, "w+", encoding="utf-8") as jsonFile:
            jsonFile.write(json.dumps(inputValue, indent=4))