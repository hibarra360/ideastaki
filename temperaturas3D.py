import numpy as np

# Definir dimensiones: 3 ciudades, 7 días, 4 semanas
num_ciudades = 3
num_dias = 7
num_semanas = 4

# Crear una matriz 3D llena de ceros
temperaturas = np.zeros((num_ciudades, num_dias, num_semanas))

# Rellenar con algunos datos de ejemplo (opcional)
# Por ejemplo, temperaturas aleatorias entre 15 y 30 grados
temperaturas = np.random.uniform(15, 30, (num_ciudades, num_dias, num_semanas))

# Mostrar la matriz de temperaturas
print(temperaturas)
