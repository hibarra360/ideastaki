# Crear una matriz bidimensional 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

# Valor a buscar
valor_a_buscar = 5

# Variable para indicar si se encontró el valor
encontrado = False

# Buscar el valor en la matriz
for fila in matriz:
    if valor_a_buscar in fila:
        encontrado = True
        break

# Mostrar mensaje de resultado
if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la matriz.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
