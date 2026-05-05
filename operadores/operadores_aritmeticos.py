# OPERADORES ARITMÉTICOS
# Operador SUMA +
# Permite SUMAR 2 valores númericos
suma = 25 + 45
print(suma)

# Permite CONCATENAR (unir) 2 cadenas de texto
concatenacion = 'Hola'+ ' ' + 'Queridos'
print(concatenacion)

#Operador RESTA
# Permite RESTAR 2 valores numericos
resta = 25 - 45
print(resta)

#Operador MULTILPICACIÓN
# Permite MULTIPLICAR 2 valores numericos
multilpicación = 25 * 45
print(multilpicación)

# Permite MULTIPLICAR una cadena de texto por un valor numerico
multilpicación_2 = 'Hola' * 3
print(multilpicación_2)

# Permite elevar un numero a una potencia
potencia = 25 ** 2
print(potencia)

#Operador DIVISIÓN
# Permite DIVIDIR 2 valores numericos
# Si el denominador es 0, la operación arrojará un erro
# ZeroDivisionError
divición = 25 / 45
print(divición)

def divison(a,b):
    try:
        resultado = a/b
        print(resultado)
    #Una vez que se sabe cual es el error especifico se pueda usar para dar un mensaje especifico en una ocación especifica
    except ZeroDivisionError:
        print('No se puede divir en 0')
    #Cuando no se sabe cual va a ser el error especifico,usar lo de abajo es una buena manera de determinar cual es el error
    except Exception as error:
        print(f'Error en la operación: {error}')

divison(25,0)

# Permite obtener el resto de una división
resto = 9 % 5
print(resto)