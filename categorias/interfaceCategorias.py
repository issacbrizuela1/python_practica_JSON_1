from categorias.categorias import Categorias
import json
import os


class InterfaceCategoria():
    def __init__(self):
        self.lista = Categorias()
        self.lista.toObjects()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def nuevoCategorias(self):
        p = Categorias()
        cadena = input("Nombre del Categorias:")
        if (len(cadena) > 0):
            p.nombre = cadena
        return p


    def mostrarCategorias(self, lista=None):
        self.cls()
        print("\n\n" + "*" * 30 + "Datos de categorias" + "*" * 30)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'Nombre'.ljust(20))
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p))
            i += 1
        input("oprime enter para continuar .....")

    def buscarCategorias(self, code):
        mylista = [p for p in self.lista if p.nombre == code]
        self.mostrarCategorias(mylista)

    def getListaCategorias(self):
        return self.lista

    def modificarCategorias(self):
        id = input("Introduce ID:")
        id = int(id)
        p = self.lista.getlist()[id]
        cadena = input("Nombre del Categorias:")
        if (len(cadena) > 0):
            p.nombre = cadena
        self.lista.modificar(id, p)

    def eliminarCategorias(self):
        id = input("Introduce ID:")
        id = int(id)
        print(self.lista.getCategorias(id))
        self.lista.eliminar(self.lista.getCategorias(id))

    def menucategorias(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "*" * 30 + "Menu de categorias" + "*" * 30)
            print("1) Nuevo Categorias")
            print("2) Modificar Categorias")
            print("3) Eliminar Categorias")
            print("4) Consultar Categorias")
            print("5) Mostrar Categorias")
            print("0) Salir")
            a = input("Selecciona una opción: ")
            if (a == '1'):
                p = self.nuevoCategorias()
                self.lista.add(p)
                self.lista.toJson(self.lista)
            elif (a == '2'):
                self.mostrarCategorias()
                self.modificarCategorias()
                self.lista.toJson(self.lista)
            elif (a == '3'):
                self.mostrarCategorias()
                self.eliminarCategorias()
                self.lista.toJson(self.lista)
            elif (a == '4'):
                codigo = input("dame el nombre:")
                self.buscarCategorias(codigo)
            elif (a == '5'):
                self.mostrarCategorias()
            elif (a == '0'):
                break
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()