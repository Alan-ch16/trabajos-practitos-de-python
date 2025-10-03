# Ejercicio 15
# importar en python una imagen a color y mostrarla. definir una funcion para convertir imagenes a color grises y mostrar el resultado no se deben usar funciones integrados, en su lugar usar la formula gris=R*o,2989 + G*0,5870 + B*0,1140

import numpy as np
from PIL import Image
import os

# 1) Cargar la imagen a color y convertirla a un arreglo NumPy
ruta_imagen = r"C:\Users\NET USO ESCOLAR 136\Documents\clases\Programacion_fede\imagen de prueba\imagen de robot.JPEG" 
imagen_color = Image.open(r"C:\Users\NET USO ESCOLAR 136\Documents\clases\Programacion_fede\imagen de prueba\imagen de robot.JPEG").convert("RGB")  # Aseguramos RGB
ancho, alto = imagen_color.size
# Convertimos a un arreglo NumPy con forma (alto, ancho, 3)
arr_color = np.asarray(imagen_color, dtype=np.uint8)

# 2) Definir la función para convertir a gris sin usar funciones integradas de conversión
def convertir_a_gris_sin_funciones_integradas(imagen_color_array):
    # Extraemos las componentes R, G, B
    R = imagen_color_array[:, :, 0].astype(np.float64)
    G = imagen_color_array[:, :, 1].astype(np.float64)
    B = imagen_color_array[:, :, 2].astype(np.float64)

    # Aplicamos la fórmula
    gris_float = R * 0.2989 + G * 0.5870 + B * 0.1140

    # Aseguramos valores dentro de [0, 255] y convertimos a uint8
    gris_clipped = np.clip(gris_float, 0, 255).astype(np.uint8)

    return gris_clipped

# 3) Usar la función para obtener la imagen en gris
arr_gris = convertir_a_gris_sin_funciones_integradas(arr_color)

# 4) Mantener formato como imagen (grises de una sola banda)
imagen_gris = Image.fromarray(arr_gris)

# 5) Mostrar ambas imágenes (opcional: guardar también)
imagen_color.show(title="Imagen a color")

imagen_gris.show(title="Imagen en gris (con la fórmula)")
