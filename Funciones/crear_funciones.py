# Dentro del lenguaje,tenemos la opción de crear nuestras PROPIAS funciones
# para eso usamos la palabra reservada DEF

def suma(num_1,num_2):
    #Este sera el contenido de la función
    resultado = num_1 + num_2
    return resultado

def resta(num_1,num_2):
    resultado = num_1 - num_2
    return resultado

def mult(num_1,num_2):
    resultado = num_1 * num_2
    return resultado

def div(num_1,num_2):
     if num_2 == 0:
         print("No se puede dividir en 0")
     else:
         resultado = num_1 / num_2
         return resultado

def pedir_datos():
    num_1 = input('Ingrese el primer número: ')
    num_2 = input('Ingrese el segundo número: ')
       
    num_1 = convertir_float(num_1)
    num_2 = convertir_float(num_2)
    
    if num_1 and num_2 != False:
        return(num_1,num_2)
    else:
        print("Ingrese un número valido")
    return(num_1,num_2)

def convertir_float(valor):
    try:
        return float(valor)
    except(ValueError, TypeError):
        return False

print()
print('Bienvenido a mi segunda calculadora')
print('======================================')
ciclo = True

while ciclo == True:
    print('\n[1] suma')
    print('[2] resta')
    print('[3] multiplicación')
    print('[4] división')
    print('[0] salir')
    opcion = input('\nSeleccione su operación [0-4]: ')

    opciones_validas = ['0','1','2','3','4']

    if opcion in(opciones_validas):
        if opcion == '0':
            ciclo = False
            print('Gracias por usar mi calculadora!')
            print('Saliendo...')
        else:
            a,b = pedir_datos()
            operacion = ''
            if a and b != False:
                if opcion == '1':
                    operacion = '+'
                    valor = suma(a,b)
                elif opcion == '2':
                    operacion = '-'
                    valor = resta(a,b)
                elif opcion == '3':
                    operacion = 'x'
                    valor = mult(a,b)
                elif opcion == '4':
                    operacion = '/'
                    valor = div(a,b)
                print(f'{a} {operacion} {b} = {valor}')
            else:
                print('Valor no corresponde')
    else:
        print('Opción NO válida.')