from db import db
import requests
import time
from PIL import Image

# Función para descargar y mostrar una imagen usando Pillow


def guardar_y_mostrar_imagen(url, nombre_archivo):
    """
    Descarga una imagen desde una URL y la muestra en una ventana aparte.
    """
    try:
        response = requests.get(url, stream=True)
        # Lanza una excepción para códigos de estado de error (4xx o 5xx)
        response.raise_for_status()

        # Determinar la extensión del archivo
        content_type = response.headers.get('Content-Type')
        extension = ".png"
        if content_type:
            if 'image/jpeg' in content_type:
                extension = '.jpg'
            elif 'image/png' in content_type:
                extension = '.png'
            elif 'image/svg+xml' in content_type:
                extension = '.svg'

        nombre_archivo_final = f"{nombre_archivo}{extension}"

        with open(nombre_archivo_final, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"\nImagen guardada exitosamente como '{nombre_archivo_final}'")
        img = Image.open(nombre_archivo_final)
        img.show()

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer el request: {e}")
    except IOError as e:
        print(f"Error al escribir el archivo o al abrir la imagen: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


class Nacionalidad:
    def __init__(self, nationality):
        self.nationality = nationality

    def search():
        objects_link = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        search_link = "https://collectionapi.metmuseum.org/public/collection/v1/search"

        # Muestra la lista de nacionalidades antes de pedir la entrada del usuario
        print("\nNacionalidades disponibles:")
        for nationality in db["Nationality"]:
            print(f"    - {nationality}")

        while True:
            print()
            nationality_input = input("""Introduzca la nacionalidad:
        --> """)

            if nationality_input not in db["Nationality"]:
                print()
                print("Introduzca una nacionalidad valida")

            else:
                break

        params = {
            "q": nationality_input,
            "hasImages": "true"
        }

        try:
            data = requests.get(search_link, params=params)
            data = data.json()

            if not data['objectIDs']:
                print("\nNo se encontraron obras con imágenes para esa nacionalidad.")
                return

            print()
            print(f"{len(data['objectIDs'])} objetos encontrados")

            valid_objects_details = []
            print("""
    Obras:
    """)

            # Bucle secuencial simple para procesar cada obra
            for object_id in data["objectIDs"]:
                try:
                    object_link = f"{objects_link}/{object_id}"
                    object_data = requests.get(object_link).json()

                    # Aquí se valida la nacionalidad y se muestra la obra
                    if object_data and object_data.get('title') and object_data.get('artistNationality') == nationality_input:
                        valid_objects_details.append(object_data)
                        print(f"{len(valid_objects_details)}.- {object_id},{object_data.get('title', 'Desconocido')},{object_data.get('artistDisplayName', 'Desconocido')},{object_data.get('artistNationality', 'Desconocido')}")

                except requests.exceptions.RequestException:
                    pass
                except (KeyError, ValueError):
                    pass

            if not valid_objects_details:
                print(
                    "No se pudieron obtener detalles de ninguna obra con esa nacionalidad. Intente con otra.")
                return

            print()
            ver = input("""Introduzca el numero de la obra que desea ver:
    --> """)

            try:
                ver = int(ver) - 1
                object_data_to_view = valid_objects_details[ver]
                object_id_to_view = object_data_to_view.get('objectId')
            except (ValueError, IndexError):
                print("Entrada inválida. Volviendo al menú principal.")
                return

            try:
                print()
                print(f"""'{object_data_to_view.get("title", "Desconocido")}' by {object_data_to_view.get("artistDisplayName", "Desconocido")},
        {object_data_to_view.get("artistNationality", "Desconocido")}, {object_data_to_view.get("artistBeginDate", "Desconocido")} - {object_data_to_view.get("artistEndDate", "Desconocido")}
        {object_data_to_view.get("classification", "Desconocido")}, {object_data_to_view.get("objectDate", "Desconocido")}
        URL de la imagen: {object_data_to_view.get("primaryImageSmall", "No disponible")}""")

                # Aquí se agrega la nueva funcionalidad para mostrar la imagen
                while True:
                    opcion_imagen = input("""\n¿Desea ver la imagen de la obra?
            1. Sí
            2. No
        --> """)

                    if opcion_imagen == "1":
                        url_imagen = object_data_to_view.get(
                            "primaryImageSmall")
                        if url_imagen:
                            guardar_y_mostrar_imagen(
                                url_imagen, f"obra_{object_id_to_view}")
                        else:
                            print("No se encontró una imagen para esta obra.")
                        break
                    elif opcion_imagen == "2":
                        break
                    else:
                        print("Opción inválida. Intente de nuevo.")

            except requests.exceptions.RequestException:
                print()
                print(
                    "No se puede mostrar la obra en estos momentos, intente nuevamente")

        except requests.exceptions.RequestException:
            print("Error con los servidores")
