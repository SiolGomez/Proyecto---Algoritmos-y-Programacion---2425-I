import requests
from PIL import Image
def guardar_imagen_desde_url(url, nombre_archivo):
    """
    Descarga una imagen desde una URL y la guarda en un archivo.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # Lanza una excepción para códigos de
        estado de error (4xx o 5xx)
        content_type = response.headers.get('Content-Type')
        extension = '.png' # Valor por defecto
    if content_type:
        if 'image/png' in content_type:
            extension = '.png'
        elif 'image/jpeg' in content_type:
            extension = '.jpg'
        elif 'image/svg+xml' in content_type:
            extension = '.svg'

    nombre_archivo_final = f"{nombre_archivo}{extension}"
    with open(nombre_archivo_final, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
            print(f"Imagen guardada exitosamente como '{nombre_archivo_final}'")
            except requests.exceptions.RequestException as e:
            print(f"Error al hacer el request: {e}")
            except IOError as e:
            print(f"Error al escribir el archivo: {e}")
            return nombre_archivo_final
            # URL de la API
            api_url = "https://images.metmuseum.org/CRDImages/ep/original/DT1567.jpg"
            # Nombre deseado para el archivo (sin extensión, ya que se determinará automáticamente
            nombre_archivo_destino = "logo_aleatorio"
            # Llamar a la función para guardar la imagen
            nombre_archivo_destino=guardar_imagen_desde_url(api_url,
            nombre_archivo_destino)
            img = Image.open(nombre_archivo_destino)
            img.show()