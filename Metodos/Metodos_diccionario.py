#Definimos un nuevo diccionario

datos_personales ={
    'nombre' : 'Antonio Morgado',
    'edad' : 19,
    'titulo' : "Analista Programador"
}

print(datos_personales)

#El metodo keys permite obtener las CLAVES del diccionario dict_keys
claves = datos_personales.keys()
print(claves)

#El metodo GET permite obtener valores de datos por su clave
nombre = datos_personales.get('nombre')
print(nombre)

#Agregamos elementos al diccionario definiendo una nueva clave con un nuevo valor
rut = input('ingrese su numero rut: ')
datos_personales['rut'] = rut
print(datos_personales)

#Eliminamos elementos de un diccionario con el metodo POP
#El metodo POP elimina un elemento por su CLAVE
datos_personales.pop('rut')
print(datos_personales)