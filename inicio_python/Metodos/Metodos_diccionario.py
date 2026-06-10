# Definimos un nuevo diccionario

datos_personales = {
    'nombre':'Erick Bailey',
    'edad':50,
    'titulo':'Analista Programador'
}

print(datos_personales)

# El método KEYS permite obtener las CLAVES del diccionario dict_keys
claves = datos_personales.keys()
print(claves)

# El método GET permite obtener valores de datos por su clave
nombre = datos_personales.get('nombre')
print(nombre)

# Agregamos elementos al diccionario definiendo una nueva clave con un nuevo valor
rut = input('Ingrese su número de rut: ')
datos_personales['rut'] = rut
print(datos_personales)

# Eliminamos elementos de un diccionario con el método POP
# El método POP elimina un elemento por su CLAVE
print('El método POP elimina un elemento por su CLAVE, eliminaremos el elemento "rut"')
datos_personales.pop('rut')
print(datos_personales)

print('\nPor defecto al recorrer un diccionario obtenemos las CLAVES')
for elemento in datos_personales:
    print(elemento)

print('\nPara recorrer los VALORES de un diccionario, usamos VALUES()')
for valor in datos_personales.values():
    print(valor)

print('\nRecorriendo ITEMS de un DICCIONARIO')
for clave,valor in datos_personales.items():
    print(f'{clave}: {valor}')

# El método CLEAR limpia completamente el diccionario
datos_personales.clear()
print(datos_personales)