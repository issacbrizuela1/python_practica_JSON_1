import os.path
import json


class JsonFile:
    def __init__(self, filename):
        self.filename = filename if filename == None else 'JSONS/Pelicula.json'

    def getDataJson(self):
        data = []
        if (os.path.isfile(self.filename)):
            file = open(self.filename, "r")
            data = json.loads(file.read())
        return data

    def toJson(self, listaClientes):
        file = open(self.filename, "w")
        file = json.dump([ob.__dict__ for ob in listaClientes], file, indent=4)