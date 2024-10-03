

# Escritura de Archivo de Texto
with open('my_notes.txt', 'w') as file:
    file.write("Primera línea de notas personales.\n")
    file.write("Segunda línea de notas personales.\n")
    file.write("Tercera línea de notas personales.\n")

# Lectura de Archivo de Texto
with open('my_notes.txt', 'r') as file:
    for line in file:
        print(line.strip())

# No es necesario cerrar el archivo explícitamente cuando se usa 'with', ya que se cierra automáticamente.
