nombre_personal = "antonio m"
titulo_personal = "Tecnico en telecomunicaciones"
ciudad = "TEMUCO"
rut_completo = "223459870"
rut_cpersonal = "22345987-0"
# El metodo Dir nos indida todos los metods disponibles para la variable
#print(dir[nombre_personal])

#Metodos de cadena, modifican el string asociado
#CAPITALIZE deja la primera letra de un string en mayuscula
print(f"Su nombre personal CAPITALIZADO: {nombre_personal.capitalize()}")
#UPPER deja toda el STRING en mayusculas
print(f"Su nombre personal MAYÚSCULAS: {nombre_personal.upper()}")
#TILTLE deja la primera letra de cada palabra en mayuscula
print(f"Su nombre personal como TITULO: {nombre_personal.title()}")
#LOWER deja todo el STRING en minusculas
print(f"Ciudad en MINUSCULAS: {ciudad.lower()}")

#COUNT cuenta la cantidad de ocurrencias de un evento o caracter
print(titulo_personal.count('x'))
#COUNT devulve 0 si no encuentra el caracter buscado

#FIND busca un SUBSTRING dentro de una cadena y devuelve el indice donde se encuentra
print(titulo_personal.find('Tecnico'))
#FIND devuelve -1 si no encuentra el SUBSTRING 

#INDEX devuelve ERROR si no encuentra el SUBSTRING, porque no puede contar el indice de lo que no existe
#print(titulo_personal.index("x"))

#El metodo LEN permite conocer el TAMAÑO (lenght/largo) de los elmentos
print(len(nombre_personal))

#Obteniendo SUBSTRING desde cadenas
#SPLIT divide la cadena de texto
titulo_personal_split = titulo_personal.split(' ')
print(titulo_personal_split)
#El resultado de SPLIT se vuelve una lista,y el caracter usado para el split se elimina
print(type(titulo_personal_split))
print(titulo_personal_split[0])

rut_split = rut_cpersonal.split('-')
print(rut_split)
print(f"Rut : {rut_split[0]}")
print(f'Digito Verificador: {rut_split[1]}')
#....


# REPLACE permite reemplazar substring dentro de una cadena de texto