import requests
from PIL import Image
import os


def guardar_y_mostrar_imagen(url, nombre_archivo):

    if not url:
        print("No hay una URL de imagen disponible para esta obra.")
        return

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        content_type = response.headers.get('Content-Type')
        extension = ".jpg"
        if content_type:
            if 'image/png' in content_type:
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
        print("No se pudo descargar la imagen. La URL podría ser inválida o el servidor no responde.")
    except IOError as e:
        print(f"Error al escribir o abrir el archivo: {e}")
        print("Asegúrese de tener los permisos necesarios para guardar archivos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
