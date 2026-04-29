import math
from crear_funciones import convertir_float

#1===================================================================================================================
#   Escribe una función que calcule el total de una factura tras aplicarle el IVA.
#       La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar.
#       Si la función no recibe el porcentaje de IVA,deberá aplicar por defecto un 10%










#2==================================================================================================================
#   Escriba una función que calcule el área de un circulo y otra que calcule
#       El volumen de un cilindro usando la primera función de área.

#a = pi x r^2
#a * altura


def area_circunferencia(radio):
    pi = math.pi
    resultado = pi * radio * radio
    return resultado

def volumen_cilindro(radio,altura):
    area = area_circunferencia(radio)
    resultado = area * altura
    return resultado

def calculo_volumen_cilindro():
    print("Ingrese los datos solicitados")
    str_radio = input('Radio: ')
    str_altura = input('altura: ')
    radio = convertir_float(str_radio)
    altura = convertir_float(str_altura)
    volumen = volumen_cilindro(radio,altura)
    print(volumen)


#3====================================================================================================================
#   Escriba una función que permita escribir la tabla de multilpicar de un numero ingresado por el usuario.
