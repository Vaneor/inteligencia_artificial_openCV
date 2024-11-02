import cv2

# Cargar una imagen desde el archivo 
image = cv2.imread('imagen.jpg')

# Mostar la imagen en una ventana
cv2.imshow('imagen', image)

# Esperar hasta que el usuario presione una tecla para cerrar la ventana
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()