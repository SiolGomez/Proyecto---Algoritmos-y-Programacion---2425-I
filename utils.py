from PIL import Image
import requests

class utils:
    def guardar_y_mostrar_imagen(url, nombre_archivo):
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