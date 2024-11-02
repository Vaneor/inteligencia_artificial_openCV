import cv2

# Cargar la imagen
image = cv2.imread('imagen.jpg')

# Definir la nueva anchura y altura
new_width, new_height = 600, 400

# Aplicar la escala a la imagen
scaled = cv2.resize(image, (new_width, new_height))

# Mostrar la imagen escalada
cv2.imshow('Escalada', scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()