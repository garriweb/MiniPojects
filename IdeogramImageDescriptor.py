import requests
from io import BytesIO
from PIL import Image

# Configura tu clave de API de Ideogram
API_KEY = "API-KEY-IDEOGRAM"  # Sustituye con tu API Key de Ideogram

# Función para descargar la imagen desde una URL
def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception(f"Error al descargar la imagen: {response.status_code}")

# Función para obtener la descripción de la imagen usando Ideogram API
def get_image_description(image_data):
    url = "https://api.ideogram.ai/describe"
    headers = {"Api-Key": API_KEY}
    files = {"image_file": image_data}

    response = requests.post(url, headers=headers, files=files)

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en la solicitud: {response.status_code}, {response.text}")

# Solicitar la URL de la imagen y generar la descripción
image_url = input("Introduce la URL de la imagen a analizar: ")

try:
    # Descargar la imagen y obtener la descripción
    image_data = download_image(image_url)
    description = get_image_description(image_data)
    print("\nDescripción de la imagen proporcionada por Ideogram:")
    print(description)
except Exception as e:
    print(str(e))