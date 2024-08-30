# Definir la matriz bidimensional 3x3 con valores numéricos
matriz = [
    [9, 3, 7],
    [4, 1, 5],
    [6, 8, 2]]


# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila_index):
    # Obtener la fila específica
    fila = matriz[fila_index]

    # Aplicar Bubble Sort para ordenar la fila en orden ascendente
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                # Intercambiar los elementos
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

    # Actualizar la fila ordenada en la matriz
    matriz[fila_index] = fila


# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila 1 ordenada:")
for fila in matriz:
    print(fila)
