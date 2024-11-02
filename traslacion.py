import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('imagen.jpg')

# Definir la matriz de traslación
tx, ty = 100, 50
M = np.float32([[1, 0, tx], [0, 1, ty]])

# Aplicar la traslación a la imagen
translated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Mostrar la imagen trasladada
cv2.imshow('Trasladada', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()