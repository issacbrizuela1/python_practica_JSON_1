import os

from actores.interfaceActores import Interface
from categorias.interfaceCategorias import InterfaceCategoria
from peliculas.interfacePelicula import InterfacePelicula

class Main():
    def __init__(self):
        self.interfaceActores = Interface()
        self.interfaceCategorias=InterfaceCategoria()
        self.interfacePelicula=InterfacePelicula()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menuPrincipal(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "*" * 40 + "Menu de Principal" + "*" * 40)
            print("C) Categorias")
            print("A) Actores")
            print("P) Peliculas")
            #print("V) Ventas")
            print("0) Salir")
            a = input("Selecciona una opción: ")
            if (a.upper() == 'C'):
                p = self.interfaceCategorias.menucategorias()
            elif (a.upper() == 'A'):
                p = self.interfaceActores.menuactores()
            elif (a.upper() == 'P'):
                p = self.interfacePelicula.menuPeliculas()
            elif (a == '0'):
                break
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()


if __name__ == '__main__':
    ip = Main()
    ip.menuPrincipal()
