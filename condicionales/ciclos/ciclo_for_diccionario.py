# Cicñp FOR (por) para iterar diccionario
# Recorro cada uno de los elementos del diccionario

datos_personal ={
    'nombre' : 'Armando Casas',
    'edad' : 35,
    'profesion' : 'constructor'
}
for clave in datos_personal:
    print(clave)

for elemento in datos_personal.items():
    print(elemento)

for elemento in datos_personal.items():
    print(f'clave : {elemento[0]}, valor: {elemento[1]}')