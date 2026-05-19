# Ciclo FOR (por) para iterar LISTAS
# Recorro cada uno de los elmentos de la lista
lista_bandas = ['P.O.D','Skilet','Demon Hunter']
nombre_peronal = 'Erick Bialey'
# Usamos el metodo RANGE para crear un rango de n´numeros
# Si a RANGE le pasamos 1 argumento, creara una lista de la cantidad agregada
# La lista inicia en el indice 0

lista_numeros = range(5)

#Si a RANGE le pasamos 2 argumentos, le indicamos desde donde inicia y el elmento final -1
lista_numeros_2 = range(10,20)

# Si a RANGE le pasamos 3 argumentos, le indicamos desde donde inicia, el elmento final -1 y el avance estre ellos
lista_numeros_3 = range(5,26,5)

banda_encontrada = False
buscar_banda = input('Que banda busca?')
for banda in lista_bandas:
    banda_mayusculas = banda.upper()
    if banda_mayusculas == buscar_banda.upper():
        banda_encontrada = True
if banda_encontrada == True:
    print('Banda encontrada')
else:
    print('Banda no encontrada')


print()
for letra in nombre_peronal:
    print(letra)

print()
print(lista_numeros)
for numero in lista_numeros:
    print(numero)
    resultado = numero * 5
    print(resultado)

print()
for elemento in lista_numeros_2:
    print(elemento)

print()
for elemento in lista_numeros_3:
    print(elemento)