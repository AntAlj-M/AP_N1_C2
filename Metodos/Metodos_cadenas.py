nombre_personal = "antonio m"
titulo_personal = "Tecnico en telecomunicaciones"
ciudad = "TEMUCO"

# El metodo Dir nos indida todos los metods disponibles para la variable
#print(dir[nombre_personal])


print(f"Su nombre personal CAPITALIZADO: {nombre_personal.capitalize()}")
print(f"Su nombre personal MAYÚSCULAS: {nombre_personal.upper()}")
print(f"Su nombre personal como TITULO: {nombre_personal.title()}")
print(f"Ciudad en MINUSCULAS: {ciudad.lower()}")

print(titulo_personal.count('e'))

print(titulo_personal.find('Tecnico'))