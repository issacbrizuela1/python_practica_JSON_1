from actores.actores import Actores
from categorias.categorias import Categorias
from peliculas.peliculas import Pelicula
import copy
import json
import os

class InterfacePelicula():
    """docstring for interfacePelicula"""
    def __init__(self):
        self.lista = Pelicula()
        self.lista.toObjects()
        self.listac = Categorias()
        self.listac.toObjects()
        self.listaA = Actores()
        self.listaA.toObjects()
    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def getlistacelicula(self):
        return self.lista
    def VerPeliculas(self, lista=None):
        self.cls()
        print("\n" + "*" * 30 + "Datos de Pelicula" + "*" * 30)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'nombre'.ljust(10) + '\t\t' + 'categoria'.ljust(10) +
              '\t\t' + 'actor'.ljust(10)+ '\t\t' + 'apellido'.ljust(10))
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t" + str(p))
            i += 1
        input("precione enter para continuar ...")
    def mostrarActores(self, lista=None):
        self.cls()
        print("\n\n" + "*" * 30 + "Datos de Actoress" + "*" * 30)
        if (lista == None):
            mylista = self.listaA
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'Nombre'.ljust(20) + '\t\t' +'apellido'.ljust(20))
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p))
            i += 1
        input("oprime enter para continuar .....")
    def mostrarCategorias(self, lista=None):
        self.cls()
        print("\n\n" + "*" * 30 + "Datos de Categorias" + "*" * 30)
        if (lista == None):
            mylista = self.listac
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'Nombre'.ljust(20))
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p))
            i += 1
        input("oprime enter para continuar .....")
    def modificarPelicula(self):
        
        pass

    def menuPeliculas(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "*" * 30 + "Menu de Pelicula" + "*" * 30)
            print("1) Nuevo Pelicula")
            print("2) Modificar Pelicula")
            print("3) Eliminar Pelicula")
            print("4) Consultar Pelicula")
            print("5) Mostrar Pelicula")
            print("0) Salir")
            a = input("Selecciona una opción: ")
            if (a == '1'):
                self.mostrarActores()
                actorid=input("seleccione el id del actor")
                aid=int(actorid)
                ACT=self.listaA.getlist()[aid]
                #
                self.mostrarCategorias()
                categoriaid=input("seleccione la categoria")
                cid=int(categoriaid)
                CATE=self.listac.getCategorias(cid)
                #
                nombrep=input("ingrese el nombre de la pelicula")
                sip=input("ingrese la sinopsis")
                p=Pelicula()
                p.nombre=nombrep
                p.nombreA=ACT
                p.nombreC=CATE
                p.sinopsis=sip
                self.lista.AgregarPelicula(p)
                self.lista.toJson(self.lista)
            elif (a == '2'):
                self.mostrarPelicula()
                self.modificarPelicula()
                self.lista.toJson(self.lista)
            elif (a == '3'):
                self.mostrarPelicula()
                self.eliminarPelicula()
                self.lista.toJson(self.lista)
            elif (a == '4'):
                codigo = input("dame el nombre:")
                self.buscarPelicula(codigo)
            elif (a == '5'):
                self.mostrarPelicula()
            elif (a == '0'):
                break;
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()