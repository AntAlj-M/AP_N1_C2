import math
#from crear_funciones import convertir_float

#1===================================================================================================================
#   Escribe una función que calcule el total de una factura tras aplicarle el IVA.
#       La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar.
#       Si la función no recibe el porcentaje de IVA,deberá aplicar por defecto un 10%

def pedir_datos_factura():
    ciclo = True
    while ciclo == True:
        str_monto = input('Ingrese el monto de la factura: ')
        monto = convertir_float(str_monto)
        if monto != None:
            ciclo = False
    str_procentaje = input('Ingrese el pordentaje de IVA\n(o deje en blanco para aplicar 19%): ')
    if str_procentaje == '':
        str_procentaje = '19'
    monto = convertir_float(str_monto)
    porcentaje = convertir_float(str_procentaje)
    factura(monto,porcentaje)

def factura(monto,porcentaje):
    if monto and porcentaje != None:
        monto_iva = monto * (porcentaje/100)
        total = monto + monto_iva
        print()
        print(f'Monto Factura: ${round(monto)}')
        print(f'Monto IVA: ${round(monto_iva)}')
        print(f'% IVA aplicado: {round(porcentaje)}')
        print(f'Total Factura: ${round(total)}')
    else:
        print('valores ingresados NO corresponden.')
#2==================================================================================================================
#   Escriba una función que calcule el área de un circulo y otra que calcule
#       El volumen de un cilindro usando la primera función de área.

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
    str_radio = input('Ingrese radio: ')
    str_altura = input('Ingrese altura: ')
    radio = convertir_float(str_radio)
    altura = convertir_float(str_altura)
    volumen = volumen_cilindro(radio,altura)
    print(f'\nEl volumen de un cilindro que cuenta con una circunferencia con area de {area_circunferencia(radio)} \n y con una altura de {str_altura} \n tiene un volumen de {volumen}\n')


#3====================================================================================================================
#   Escriba una función que permita escribir la tabla de multilpicar de un numero ingresado por el usuario.

def tabla():
    str_numero = input('Ingrese un número: ')
    numero = convertir_float(str_numero)
    factor = 1
    if numero != None:
        while factor <= 12:
            total = numero * factor
            print(f'{numero} x {factor} = {total}')
            factor += 1
#4=====================================================================================================================

def convertir_float(valor):
    try:
        return float(valor)
    except ValueError:
        print('El valor ingresado NO se puede convertir a número.')
    except Exception as error:
        print(f'Se ha producido el siguiente error: {error}')
        print(f'Tipo de error: {type(error)}')
        print(f'Argumentos del error: {error.args}')
        return None





#5=====================================================================================================================

while True:
    print('[1] Cálculo IVA')
    print('[2] Cálculo Volumen Cilindro')
    print('[3] Tabla de Multiplicar')
    print('[0] Salir')

    opcion = input('\nIngrese su Opción [0-3]\n')
    opcion = float(opcion)
    valores_opcion = range(4)

    if opcion in valores_opcion:
        if opcion == 1:
            pedir_datos_factura()
        elif opcion == 2:
            calculo_volumen_cilindro()
        elif opcion == 3:
            tabla()
        elif opcion == 0:
            print('Saliendo del sistema...')
            break
    else:
        print('Opción ingresada NO corresponde...')