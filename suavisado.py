import cv2

# Cargar la imagen
image = cv2.imread('imagen.jpg')    

# Aplicar el filtro de Gaussiano para suavizar la imagen
smoothed = cv2.GaussianBlur(image, (5, 5), 0)

# Mostrar la imagen suavizada
cv2.imshow('Suavizada', smoothed)
cv2.waitKey(0)
cv2.destroyAllWindows()
