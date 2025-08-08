from Nacionalidad import Nacionalidad
from Departamento import Departamento
from Nombre import Nombre

class Museo:
    def start(self):

        """
        Comienza la interfaz del museo en la terminal, el usuario luego debe elegir la opcion a utilizar
        """
        
        while True:
            print()
            menu = input("""Bienvenido a MetroArt, elija una opcion:
                            
            1. Ver lista de obras por departamento 
            2. Ver lista de obras por nacionalidad del autor
            3. Ver lista de obras por nombre del autor
            4. Salir
                                
        --> """)
            
            if menu == "1":
                print()
                Departamento.search()

            elif menu == "2":
                print()
                Nacionalidad.search()

            elif menu == "3":
                print()
                Nombre.search()

            elif menu == "4":
                break

            else:
                print()
                print("Opcion invalida")
