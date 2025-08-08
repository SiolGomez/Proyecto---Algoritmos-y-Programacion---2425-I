import requests
import time

class Departamento:
    def __init__(self,department):
        self.department = department
    
    def show(self):
        print(f"Departamentos: ")
        for department in self.department:
            print(f"    {department}")

    def search():
        objects_link = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        search_link = "https://collectionapi.metmuseum.org/public/collection/v1/search"
        departments_link = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

        data = requests.get(departments_link)
        data = data.json()

       
        print(f"Departamentos: ")
        for departamento in data["departments"]:
            print(f"    {departamento["departmentId"]} - {departamento["displayName"]}")
            print()
               
            
        while True: 

            department_input = input("""Introduzca el nombre del departamento:
            --> """)
 

            params = {
                "q": department_input,
                "hasImages": "true"
            }

            try:
                data = requests.get(search_link,params=params)
                data = data.json()

                print()
                print(f"{data['total']} objetos encontrados")

                objects = []

                for id in data["objectIDs"]:
                    objects.append(id)

                print("""
        Obras:
        """)
                for i in range(len(objects)):

                    try:
                        object_link = f"{objects_link}/{objects[i]}"
                        object_data = requests.get(object_link)
                        object_data = object_data.json()

                        if department_input == object_data["department"]:
                            print(f"{i+1}.- {object_data["objectID"]}, {object_data["title"]}, {object_data["artistDisplayName"]}")

                    except ValueError:
                        print("No se pudo obtener este item")

                        while True:
                            print()
                            seguir = input("""Quiere seguir mostrando obras?
                1. Si
                2. Ver obra
                3. No
            --> """)

                            if seguir == "1":
                                print()
                                break

                            elif seguir == "2":
                                print()
                                ver = input("""Introduzca el ID de la obra para ver su informacion:        
            --> """)

                                try:
                                    object_link = f"{objects_link}/{ver}"
                                    object_data = requests.get(object_link)
                                    object_data = object_data.json()

                                    print()

                                    print(f"""'{object_data["title"]}' by {object_data["artistDisplayName"]},
        {object_data["artistNationality"]}, {object_data["artistBeginDate"]} - {object_data["artistEndDate"]}
        {object_data["classification"]}, {object_data["objectDate"]}
        {object_data["primaryImageSmall"]}""")

                                except ValueError:
                                    print()
                                    print("No se puede mostrar la obra en estos momentos, intente nuevamente")

                                    while True:
                                        try_again = input("""
                1. Intentar de nuevo
                2. Salir                
            --> """)
                                        if try_again == "1":
                                            try:
                                                object_link = f"{objects_link}/{ver}"
                                                object_data = requests.get(object_link)
                                                object_data = object_data.json()

                                                print()
                                                print(f"""'{object_data["title"]}' by {object_data["artistDisplayName"]},
                    {object_data["artistNationality"]}, {object_data["artistBeginDate"]} - {object_data["artistEndDate"]}
                    {object_data["classification"]}, {object_data["objectDate"]}
                    {object_data["primaryImageSmall"]}""")
                                                break

                                            except ValueError:
                                                print()
                                                print("No se puede mostrar la obra en estos momentos, intente nuevamente")
                                        elif try_again == "2":
                                            break
                                        else:
                                            print("Opcion invalida")

                            elif seguir == "3":
                                return

                            else:
                                print()
                                print("Opcion invalida")
                
                print("")
                print("Se han mostrado todos los objetos")

                while True:
                    print()
                    ver = input("""Introduzca el ID de la obra para ver su informacion:        
            --> """)

                    try:
                        object_link = f"{objects_link}/{ver}"
                        object_data = requests.get(object_link)
                        object_data = object_data.json()

                        print()
                        print(f"""'{object_data["title"]}' by {object_data["artistDisplayName"]},
            {object_data["artistNationality"]}, {object_data["artistBeginDate"]} - {object_data["artistEndDate"]}
            {object_data["classification"]}, {object_data["objectDate"]}
            {object_data["primaryImageSmall"]}""")

                    except ValueError:
                        print()
                        print("No se puede mostrar la obra en estos momentos, intente nuevamente")

                        while True:
                            try_again = input("""
                1. Intentar de nuevo
                2. Salir                 
            --> """)
                            if try_again == "1":
                                try:
                                    object_link = f"{objects_link}/{ver}"
                                    object_data = requests.get(object_link)
                                    object_data = object_data.json()

                                    print()
                                    print(f"""'{object_data["title"]}' by {object_data["artistDisplayName"]},
            {object_data["artistNationality"]}, {object_data["artistBeginDate"]} - {object_data["artistEndDate"]}
            {object_data["classification"]}, {object_data["objectDate"]}
            {object_data["primaryImageSmall"]}""")
                                    break

                                except ValueError:
                                    print()
                                    print("No se puede mostrar la obra en estos momentos, intente nuevamente")
                            elif try_again == "2":
                                return
                            else:
                                print("Opcion invalida")
                
            except ValueError:
                print("Error con los servidores")    

    


                    
            
        
            
                    