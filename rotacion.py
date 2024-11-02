import cv2 
import numpy as np 

# Cargar la imagen
image = cv2.imread('imagen.jpg')

# Obtener las dimensiones de la imagen
height, width = image.shape[:2]

# Calcular el centro de la imagen
center = (width / 2, height / 2)

# Definir la matriz de rotación
angle = 45
M = cv2.getRotationMatrix2D(center, angle, 1.0)

# Aplicar la rotación de la imagen
rotated = cv2.warpAffine(image, M, (width, height))

# Mostrar la imagen rotada
cv2.imshow('Rotada', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
