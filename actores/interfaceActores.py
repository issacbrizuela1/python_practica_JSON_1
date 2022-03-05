from actores.actores import Actores
import json
import os


class Interface():
    def __init__(self):
        self.lista = Actores();
        self.lista.toObjects();

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def nuevoActores(self):
        p = Actores()
        cadena = input("Nombre del Actores:")
        if (len(cadena) > 0):
            p.nombreA = cadena
        cadena = input("Apellido del Actores:")
        if (len(cadena) > 0):
            p.apellidoA = cadena
        return p


    def mostrarActores(self, lista=None):
        self.cls()
        print("\n\n" + "*" * 30 + "Datos de actores" + "*" * 30)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'Nombre'.ljust(20)+ 'Apellido'.ljust(20))
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p))
            i += 1
        input("oprime enter para continuar .....")

    def buscarActores(self, code):
        mylista = [p for p in self.lista if p.nombreA == code]
        self.mostrarActores(mylista)

    def getListaActores(self):
        return self.lista

    def modificarActores(self):
        id = input("Introduce ID:")
        id = int(id)
        p = self.lista.getlist()[id]
        cadena = input("Nombre del Actores:")
        if (len(cadena) > 0):
            p.nombreA = cadena
        cadena = input("Apellido del Actores:")
        if (len(cadena) > 0):
            p.apellidoA = cadena
        self.lista.modificar(id, p)

    def eliminarActores(self):
        id = input("Introduce ID:")
        id = int(id)
        print(self.lista.getActores(id))
        self.lista.eliminar(self.lista.getActores(id))

    def menuactores(self):
        a = 10;
        while a != 0:
            self.cls()
            print("\n\n" + "*" * 30 + "Menu de actores" + "*" * 30)
            print("1) Nuevo Actores")
            print("2) Modificar Actores")
            print("3) Eliminar Actores")
            print("4) Consultar Actores")
            print("5) Mostrar Actores")
            print("0) Salir")
            a = input("Selecciona una opción: ")
            if (a == '1'):
                p = self.nuevoActores()
                self.lista.add(p)
                self.lista.toJson(self.lista)
            elif (a == '2'):
                self.mostrarActores()
                self.modificarActores()
                self.lista.toJson(self.lista)
            elif (a == '3'):
                self.mostrarActores()
                self.eliminarActores()
                self.lista.toJson(self.lista)
            elif (a == '4'):
                codigo = input("dame el nombre:")
                self.buscarActores(codigo)
            elif (a == '5'):
                self.mostrarActores()
            elif (a == '0'):
                break;
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()