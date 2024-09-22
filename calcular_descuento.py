# Definir la función calcular_descuento
def calcular_descuento(precio, porcentaje_descuento):
    descuento = precio * (porcentaje_descuento / 100)
    precio_final = precio - descuento
    return precio_final

# Llamar a la función con un ejemplo
precio_original = 100  # Precio en unidades monetarias
descuento = 20  # Porcentaje de descuento
precio_con_descuento = calcular_descuento(precio_original, descuento)

print(f"El precio final con un {descuento}% de descuento es: {precio_con_descuento}")
