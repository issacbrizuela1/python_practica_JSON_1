from peliculas.jsonPeliculafile import JsonFile
from actores.actores import Actores
from categorias.categorias import Categorias


class Pelicula(JsonFile,Actores,Categorias):
    def __init__(self, nombre='',sinopsis='',nombreA='',apellidoA='',nombreC='', lista=list()):
        super(Pelicula, self).__init__('JSONS/peliculas.json')
        self.nombre = nombre
        self.sinopsis = sinopsis
        self.nombreA=nombreA
        self.apellidoA=apellidoA
        self.nombreC=nombreC
        self.lista = lista
        self.__idx__ = 0
        self.nombrefile = "JSONS/Pelicula.json"

    def AgregarPelicula(self, Pelicula):
        self.lista.append(Pelicula)

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
            lista.append(
                Pelicula(nombre=x['nombre'], sinopsis=x['sinopsis'],nombreA=x["nombreA"],apellidoA=x["apellidoA"], nombreC=x["nombreC"]))
        self.lista = lista
    def __str__(self):
        return (self.nombre).ljust(20) + ' \t\t' + (self.sinopsis).ljust(20) + ' \t\t' + (self.nombreA).ljust(
            20) + ' \t\t' + (self.apellidoA).ljust(20) + ' \t\t' + (self.nombreC).ljust(20)
    def eliminarPelicula(self, Pelicula):
        self.lista.remove(Pelicula)
    def getPelicula(self, index):
        return self.lista[index]
    def modificarPelicula(self, index, Pelicula):
        self.lista[index] = Pelicula

    def tamano(self):
        return len(self.lista)

    def getlist(self):
        return self.lista

    def getDictory(self):
        return {
            "nombre pelicula":self.nombre,
            "sinopsis":self.sinopsis,
            "autor":self.nombreA,
            "apellido":self.apellidoA,
            "categoria":self.nombreC
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
