from actores.jsonActoresfile import JsonFile


class Actores(JsonFile):
    def __init__(self, nombreA='',apellidoA='', lista=list()):
        super(Actores, self).__init__('JSONS/actores.json')
        self.nombreA = nombreA
        self.apellidoA = apellidoA
        self.lista = lista
        self.__idx__ = 0
        self.nombreAfile = "JSONS/actores.json"

    def add(self, Actores):
        self.lista.append(Actores)

    def eliminar(self, Actores):
        self.lista.remove(Actores)

    def getActores(self, index):
        return self.lista[index]

    def modificar(self, index, Actores):
        self.lista[index] = Actores

    def tamano(self):
        return len(self.lista)

    def getlist(self):
        return self.lista

    def __str__(self):
        return self.nombreA.ljust(20) + self.apellidoA.ljust(20)

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
            lista.append(Actores(nombreA=x['nombre'],apellidoA=x['apellido']))
        self.lista = lista

    def getDictory(self):
        return {
            "nombreA": self.nombreA,
            "apellidoA": self.apellidoA,
        }

    def listDict(self):
        listDiccionario = list()
        for x in self.lista:
            listDiccionario.append(x.__dict__)
            print(x.getDictory())
        return listDiccionario

    def __iter__(self):
        self.__idx__ = 0
        return self

    def __next__(self):
        if self.__idx__ < len(self.lista):
            x = self.lista[self.__idx__]
            self.__idx__ += 1
            return x
        else:
            raise StopIteration
