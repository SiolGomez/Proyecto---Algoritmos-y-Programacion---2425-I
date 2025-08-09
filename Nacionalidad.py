from utils import utils
from db import db
import requests

class Nacionalidad:

    def search():

        """
        Muestra las obras por Nacionalidad, la cual es introducida por el usuario
        """

        objects_link = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        search_link = "https://collectionapi.metmuseum.org/public/collection/v1/search"

        while True:
            print()
            opcion = input("""Escoja la inicial de la nacionalidad para mostrar las opciones
        1. A-I
        2. J-R
        3. S-Z
    --> """)
            if opcion not in ("1","2","3"):
                print()
                print("Elija una opcion valida")
                continue

            print()
            for nationality in db:
                inicial = nationality[0].upper()

                if opcion == "1":
                    if "A" <= inicial <= "I":
                        print(f"        {nationality}")
                elif opcion == "2":
                    if "J" <= inicial <= "R":
                        print(f"        {nationality}")
                elif opcion == "3":
                    if "S" <= inicial <= "Z":
                        print(f"        {nationality}")

            print()
            nationality_input = input("""Introduzca la nacionalidad:
        --> """)

            if nationality_input not in db:
                print()
                print("Introduzca una nacionalidad valida")

            else:
                break

        params = {
            "q": nationality_input,
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

                    if nationality_input == object_data["artistNationality"]:
                        print(f"        {object_data["objectID"]}, {object_data["title"]}, {object_data["artistDisplayName"]}")

                except (ValueError, KeyError, TypeError):
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
                            ver = input("""Introduzca el ID de la obra para ver su informacion o marque 0 para volver:        
        --> """)
                            if ver == "0":
                                break

                            elif int(ver) not in objects:
                                print()
                                print("El ID del objeto no se encuentra en la lista de obras")
                                continue
        
                            else:
                                try:
                                    object_link = f"{objects_link}/{ver}"
                                    object_data = requests.get(object_link)
                                    object_data = object_data.json()

                                    print()

                                    print(f"""'{object_data["title"]}' by {object_data["artistDisplayName"]},
{object_data["artistNationality"]}, {object_data["artistBeginDate"]} - {object_data["artistEndDate"]}
{object_data["classification"]}, {object_data["objectDate"]}
{object_data["primaryImageSmall"]}""")
                                    
                                    while True:
                                        image = input("""Desea ver la imagen?
            1. Si
            2. No
        --> """)
                                        if image == "1":
                                            utils.guardar_y_mostrar_imagen(object_data["primaryImageSmall"],f"{object_data["objectID"]}")
                                            break

                                        elif image == "2":
                                            break
                                        else:
                                            print("Opcion Invalida")

                                except (ValueError, KeyError, TypeError):
                                    print()
                                    print("No se puede mostrar la obra en estos momentos, intente nuevamente")

                                    while True:
                                        try_again = input("""
            1. Intentar de nuevo
            2. Volver                
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
                                                while True:
                                                    image = input("""Desea ver la imagen?
            1. Si
            2. No
        --> """)
                                                    if image == "1":
                                                        utils.guardar_y_mostrar_imagen(object_data["primaryImageSmall"],f"{object_data["objectID"]}")
                                                        break

                                                    elif image == "2":
                                                        break
                                                    else:
                                                        print("Opcion Invalida")

                                            except (ValueError, KeyError, TypeError):
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
                ver = input("""Introduzca el ID de la obra para ver su informacion o marque 0 para volver:        
        --> """)
                
                if ver == "0":
                        break

                elif int(ver) not in objects:
                    print()
                    print("El ID del objeto no se encuentra en la lista de obras")
                    continue

                try:
                    object_link = f"{objects_link}/{ver}"
                    object_data = requests.get(object_link)
                    object_data = object_data.json()

                    print()
                    print(f"""'{object_data["title"]}' by {object_data["artistDisplayName"]},
{object_data["artistNationality"]}, {object_data["artistBeginDate"]} - {object_data["artistEndDate"]}
{object_data["classification"]}, {object_data["objectDate"]}
{object_data["primaryImageSmall"]}""")
                    
                    while True:
                        image = input("""Desea ver la imagen?
            1. Si
            2. No
        --> """)
                        if image == "1":
                            utils.guardar_y_mostrar_imagen(object_data["primaryImageSmall"],f"{object_data["objectID"]}")
                            break

                        elif image == "2":
                            break
                        else:
                            print("Opcion Invalida")

                except (ValueError, KeyError, TypeError):
                    print()
                    print("No se puede mostrar la obra en estos momentos, intente nuevamente")

                    while True:
                        try_again = input("""
            1. Intentar de nuevo
            2. Volver                 
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
                                
                                while True:
                                    image = input("""Desea ver la imagen?
            1. Si
            2. No
        --> """)
                                    if image == "1":
                                        utils.guardar_y_mostrar_imagen(object_data["primaryImageSmall"],f"{object_data["objectID"]}")
                                        break

                                    elif image == "2":
                                        break
                                    else:
                                        print("Opcion Invalida")
                                
                                break

                            except (ValueError, KeyError, TypeError):
                                print()
                                print("No se puede mostrar la obra en estos momentos, intente nuevamente")
                        elif try_again == "2":
                            return
                        else:
                            print("Opcion invalida")
            
        except (ValueError, KeyError, TypeError):
            print()
            print("Error con los servidores")