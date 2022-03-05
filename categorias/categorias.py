from categorias.jsonCategoriasfile import JsonFile


class Categorias(JsonFile):
    def __init__(self, nombreC='', lista=list()):
        super(Categorias, self).__init__('JSONS/categorias.json')
        self.nombreC = nombreC
        self.lista = lista
        self.__idx__ = 0
        self.nombrefile = "JSONS/categorias.json"

    def add(self, Categorias):
        self.lista.append(Categorias)

    def eliminar(self, Categorias):
        self.lista.remove(Categorias)

    def getCategorias(self, index):
        return self.lista[index]

    def modificar(self, index, Categorias):
        self.lista[index] = Categorias

    def tamano(self):
        return len(self.lista)

    def getlist(self):
        return self.lista

    def __str__(self):
        return self.nombreC.ljust(20) 

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
            lista.append(Categorias(nombreC=x['nombre']))
        self.lista = lista

    def getDictory(self):
        return {
            "nombreC": self.nombreC
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
