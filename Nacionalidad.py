from db import db
import requests
import time
from utils import guardar_y_mostrar_imagen


class Nacionalidad:
    def __init__(self, nationality):
        self.nationality = nationality

    def search(self):
        objects_link = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        search_link = "https://collectionapi.metmuseum.org/public/collection/v1/search"

        print("Nacionalidades disponibles:")
        for i, nac in enumerate(self.nationality):
            print(f"{i+1}. {nac}")

        while True:
            try:
                nationality_input_index = int(
                    input("\nIntroduzca el número de la nacionalidad: \n--> ")) - 1
                if 0 <= nationality_input_index < len(self.nationality):
                    nationality_input = self.nationality[nationality_input_index]
                    break
                else:
                    print(
                        "Opción inválida. Por favor, introduzca un número de la lista.")
            except ValueError:
                print("Entrada inválida. Por favor, introduzca un número.")

        params = {
            "q": nationality_input,
            "hasImages": "true"
        }

        try:
            data = requests.get(search_link, params=params)
            data.raise_for_status()
            data = data.json()

            print()
            print(f"{data.get('total', 0)} objetos encontrados")

            if data.get('objectIDs'):
                objects = data['objectIDs']
                filtered_objects_data = []

                print("Obras encontradas (filtrando por nacionalidad):")
                for object_id in objects:
                    try:
                        object_link = f"{objects_link}/{object_id}"
                        object_data = requests.get(object_link)
                        object_data.raise_for_status()
                        object_data = object_data.json()

                        if object_data.get("artistNationality") and nationality_input.lower() in object_data.get("artistNationality", "").lower():
                            filtered_objects_data.append(object_data)
                            print(
                                f"ID: {object_data.get('objectID', 'N/A')}, Título: {object_data.get('title', 'Sin Título')}, Autor: {object_data.get('artistDisplayName', 'Desconocido')}")
                    except requests.exceptions.RequestException:
                        continue

                if not filtered_objects_data:
                    print(
                        "No se encontraron obras con la nacionalidad especificada después de filtrar.")

            else:
                print("No se encontraron objetos para la nacionalidad seleccionada.")

            while True:
                ver_obra_id = input(
                    "\n¿Desea ver los detalles de una obra? (Introduzca el ID o 'salir'):\n--> ")
                if ver_obra_id.lower() == 'salir':
                    break

                try:
                    object_link_to_view = f"{objects_link}/{ver_obra_id}"
                    object_data_to_view = requests.get(object_link_to_view)
                    object_data_to_view.raise_for_status()
                    object_data_to_view = object_data_to_view.json()

                    print(f"\nDetalles de la obra con ID {ver_obra_id}:")
                    print(
                        f"'{object_data_to_view.get('title', 'Sin Título')}' por {object_data_to_view.get('artistDisplayName', 'Desconocido')},")
                    print(f"  {object_data_to_view.get('artistNationality', 'Desconocido')}, {object_data_to_view.get('artistBeginDate', 'Desconocido')} - {object_data_to_view.get('artistEndDate', 'Desconocido')}")
                    print(
                        f"  {object_data_to_view.get('classification', 'Desconocido')}, {object_data_to_view.get('objectDate', 'Desconocido')}")
                    print(
                        f"  URL de la imagen: {object_data_to_view.get('primaryImageSmall', 'No disponible')}")

                    while True:
                        opcion_imagen = input(
                            "\n¿Desea ver la imagen de la obra? (1. Sí, 2. No)\n--> ")
                        if opcion_imagen == "1":
                            url_imagen = object_data_to_view.get(
                                "primaryImageSmall")
                            if url_imagen:
                                guardar_y_mostrar_imagen(
                                    url_imagen, f"obra_{ver_obra_id}")
                            else:
                                print("No se encontró una imagen para esta obra.")
                            break
                        elif opcion_imagen == "2":
                            break
                        else:
                            print("Opción inválida. Intente de nuevo.")

                except requests.exceptions.RequestException:
                    print(
                        f"No se pudo encontrar o mostrar la obra con ID {ver_obra_id}.")

        except requests.exceptions.RequestException:
            print("Error con los servidores. No se pudo realizar la búsqueda.")
