# Dentro del lenguaje,tenemos la opción de crear nuestras PROPIAS funciones
# para eso usamos la palabra reservada DEF

def suma(num_1,num_2):
    #Este sera el contenido de la función
    resultado = num_1 + num_2
    print(f'{num_1} + {num_2} = {resultado}')

def resta(num_1,num_2):
    resultado = num_1 - num_2
    print(f'{num_1} - {num_2} = {resultado}')

def mult(num_1,num_2):
    resultado = num_1 * num_2
    print(f'{num_1} X {num_2} = {resultado}')

def div(num_1,num_2):
     if num_2 == 0:
         print("No se puede dividir en 0")
     else:
         resultado = num_1 / num_2
         print(f'{num_1} / {num_2} = {resultado}')

def pedir_datos():
    num_1 = input('Ingrese el primer número: ')
    num_2 = input('Ingrese el segundo número: ')
       
    if num_1.isdigit() and num_2.isdigit():
        num_1 = float (num_1)
        num_2 = float (num_2)
    else:
        print("Ingrese un número valido")
    return(num_1,num_2)

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
    opciom = input('\n Seleccione su operación [0-4] : ')

    if opciom == '0':
        ciclo = False
        print('Gracias por usar mi calculadora')
        print('Saliendo...')
    
    a,b = pedir_datos()
    if opciom == '1':
        suma(a,b)
    elif opciom == '2':
        resta(a,b)
    elif opciom == '3':
        mult(a,b)
    elif opciom == '4':
        div(a,b)
    else:
        print('Elija una opción valida')