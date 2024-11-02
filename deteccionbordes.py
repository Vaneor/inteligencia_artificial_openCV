import cv2

# Cargar la imagen en escala de grises
image = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el operador Sobel para detectar bordes 

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

# Combinar las respuestas en magnitud
edges = cv2.magnitude(sobelx, sobely)

# Normalizar los valores para mostrar la imagen correctamente
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX)

# Mostrar la imagen con los bordes detectados
cv2.imshow('Deteccion de bordes', edges)
cv2.waitKey(0)  
cv2.destroyAllWindows()