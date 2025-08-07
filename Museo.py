from Nacionalidad import Nacionalidad
from Departamento import Departamento

class Museo:
    def __init__(self,db):
        self.db = db

    def start(self):
        
        while True:
            print()
            menu = input("""Bienvenido a MetroArt, elija una opcion:
                            
        1. Ver lista de obras por Departamento 
        2. Ver lista de obras por Nacionalidad del autor
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

            else:
                print()
                print("Opcion invalida")


    def load_data(self):

        self.objects = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        self.searchs = "https://collectionapi.metmuseum.org/public/collection/v1/search"
        self.departments = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

        self.nationality = []