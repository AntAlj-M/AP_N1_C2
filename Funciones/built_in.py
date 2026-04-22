import math
# BUILT IN son funciones que ya existe dentro del lenguaje

#PRINT es una función que muestra por pantalla (terminal o linea de comandos) el argumento entregado

print('Es es el ARGUMENTO de la función')

#El metodo/función,ROUND redondea un número a una cantidad especifica de decimales
print(round(math.pi,3))

lista_numeros = [10,20,30,40,50]
#El metodo SUM realiza una suma de elementos de tipo numero, entregados como argumento
print(sum(lista_numeros))
print(sum([1,5,9,7,5,3]))

#El metodo permite al usuario ingresar datos,que SIEMPRE seran de tipo STR
nombre = input('Ingrese su nombre: ')
print(nombre)