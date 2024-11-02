import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('imagen.jpg')

# Definir el kernel para el filtro de afilado
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

# Aplicar el filtro de afilado para realzar los detalles
sharpened = cv2.filter2D(image, -1, kernel)

# Mostrar la imagen realzada    
cv2.imshow('Realzada', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
