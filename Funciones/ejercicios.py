import math
#from crear_funciones import convertir_float

#1===================================================================================================================
#   Escribe una función que calcule el total de una factura tras aplicarle el IVA.
#       La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar.
#       Si la función no recibe el porcentaje de IVA,deberá aplicar por defecto un 10%

def pedir_datos_facturas():
    monto = input('Ingrese el monto: ')
    porcentaje = input('Ingrese el porcentaje de IVA,o dejar en blanco para usar el IVA por defecto (10%) ')
    if porcentaje == False:
        porcentaje = 10
    monto = convertir_float(monto)
    porcentaje = convertir_float(porcentaje)
    factura(monto,porcentaje)

def convertir_float(valor):
    try:
        return float(valor)
    except(ValueError, TypeError):
        return False

def factura (monto,porcentaje):
    total = monto + (monto * (porcentaje/100))
    print(f'\nLa factura con monto de {monto} y con IVA de {porcentaje} tiene un total de {total}\n')
    return total








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
    print(f'\nEl volumen de un cilindro que cuenta con una circunferencia con area de {area_circunferencia(radio)} \n y con una altura de {str_altura} \n tiene un volumen de {volumen}\n')


#3====================================================================================================================
#   Escriba una función que permita escribir la tabla de multilpicar de un numero ingresado por el usuario.

def tabla():
    numero = input('Ingrese un número: ')
    numero = float(numero)
    factor = 1
    while factor <= 12:
        total = numero * factor
        print(f'\nEl número {numero} multiplicado por el factor {factor} da un total de {total}\n')
        factor = factor + 1


















while True:
    print('[1] Cálculo IVA')
    print('[2] Cálculo Volumen Cilindro')
    print('[3] Tabla de Multiplicar')
    print('[0] Salir')

    opcion = input('Ingrese su Opción [0-3]')
    opcion = float(opcion)
    valores_opcion = range(4)

    if opcion in valores_opcion:
        if opcion == 1:
            pedir_datos_facturas()
        elif opcion == 2:
            calculo_volumen_cilindro()
        elif opcion == 3:
            tabla()
        elif opcion == 0:
            print('Saliendo del sistema...')
            break
    else:
        print('Opción ingresada NO corresponde...')