from Nacionalidad import Nacionalidad

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
            
            if menu == "2":
                print()
                for nacionalidad in self.nationality:
                    nacionalidad.show()

            else:
                print()
                print("Opcion invalida")


    def load_data(self):
        nationality_list = self.db["Nationality"]

        self.nationality = []

        self.nationality.append(Nacionalidad(nationality_list))