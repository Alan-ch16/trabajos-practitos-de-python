#ejercicio 14
#importar en python una imagen en escala de grises y almacenada en una matriz mostrar la imagen en pantalla.luego ordenar los valores numericos para voltear  la imagen horizontalmente y mostrar el resultado en pantalla

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises con Pillow
imagen = Image.open(r"C:\Users\NET USO ESCOLAR 136\Pictures\imagen de prueba\imagen de robot.jpeg").convert("L") # "L" = modo grayscale
matriz = np.array(imagen)  # Convertir a matriz NumPy

# Mostrar la imagen original
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(matriz, cmap="gray")
plt.axis("off")

# Voltear horizontalmente la imagen (invertir cada fila)
matriz_volteada = np.fliplr(matriz)

# Mostrar la imagen volteada
plt.subplot(1, 2, 2)
plt.title("Volteada (Horizontal)")
plt.imshow(matriz_volteada, cmap="gray")
plt.axis("off")

plt.show()
