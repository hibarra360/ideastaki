
# Definir la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función con solo el monto total de la compra
monto_total_1 = 100.0
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1

# Llamada a la función con el monto total de la compra y el porcentaje de descuento
monto_total_2 = 200.0
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2

# Mostrar los resultados
print(f"Compra 1: Monto total = ${monto_total_1}, Descuento = ${descuento_1}, Monto final = ${monto_final_1}")
print(f"Compra 2: Monto total = ${monto_total_2}, Descuento = ${descuento_2}, Monto final = ${monto_final_2}")

