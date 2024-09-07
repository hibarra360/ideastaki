# Importar la biblioteca numpy para manejar matrices
import numpy as np

# Definir las dimensiones de la matriz
ciudades = ["Ciudad1", "Ciudad2", "Ciudad3"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Número de semanas

# Crear una matriz 3D con ceros
temperaturas = np.zeros((len(ciudades), len(dias_semana), semanas))

# Llenar la matriz con datos de ejemplo (temperaturas aleatorias)
for i in range(len(ciudades)):
    for j in range(len(dias_semana)):
        for k in range(semanas):
            temperaturas[i, j, k] = np.random.uniform(15, 35)  # Temperaturas entre 15 y 35 grados

# Mostrar la matriz
print("Matriz de temperaturas diarias:")
print(temperaturas)
