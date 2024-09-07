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

# Calcular el promedio de temperaturas para una ciudad por cada semana
ciudad_index = 0  # Índice de la ciudad para la cual queremos calcular el promedio (por ejemplo, Ciudad1)
promedios_semanales = []

for k in range(semanas):
    suma_temperaturas = 0
    for j in range(len(dias_semana)):
        suma_temperaturas += temperaturas[ciudad_index, j, k]
    promedio_semanal = suma_temperaturas / len(dias_semana)
    promedios_semanales.append(promedio_semanal)

# Mostrar los promedios semanales
print(f"Promedios semanales de temperaturas para {ciudades[ciudad_index]}:")
for semana, promedio in enumerate(promedios_semanales, start=1):
    print(f"Semana {semana}: {promedio:.2f} grados")
