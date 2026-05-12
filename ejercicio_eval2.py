# Los ejercicios a resolver deben incluirse dentro de un menú
# mediante el cual se ejecutará cada uno de ellos.

# 1.- Escriba una función que al ser llamada imprima el saludo "Buen día!"

def saludo_cordial():
    saludo = '!Buen día!'
    return saludo

# 2.- Escriba una función que solicite al usuario ingresar su nombre
# en una variable nombre_usuario
# y al ser llamada imprima el saludo "Buen día 'nombre_usuario'!"

def saludo_personal():
    saludo = saludo_cordial()
    saludo_mod = saludo.split('!')
    saludo_mod_2 = saludo.replace('!',' ')
    nombre_usuario = solicitar_nombre_usuario()
    saludo_1_split = saludo_mod[0] + ' ' + nombre_usuario + '!'
    saludo_2_split = f'{saludo_mod[0]} {nombre_usuario}!'
    saludo_1_replace = saludo_mod_2 + nombre_usuario + '!'
    saludo_2_replace = f'{saludo_mod_2}{nombre_usuario}!'
    print(saludo_1_split + '\n' + saludo_2_split + '\n' + saludo_1_replace + '\n' + saludo_2_replace)

def solicitar_nombre_usuario():
    nombre_usuario = input('Ingrese su nombre: ')
    return nombre_usuario.title()

# 3.- Escribir una función que pida al usuario un número entero menor a 10
# y al ser llamada entregue el factorial de ese número

def numero_factorial():
    ciclo = True
    while ciclo == True:
        str_numero = input('Ingrese un numero menor a 10: ')
        try:
            num = int(str_numero)
        except ValueError:
            num = None

        if num == None:
            print('Valor no corresponde a un número')
        else:
            if num < 10:
                rango = range(1,num + 1) 
                factorial = 1
                for numero in rango:
                    factorial *= numero
                print(factorial)
                ciclo = False
            elif num >= 10:
                print('Ingrese un número valido')
            
            


def menu_principal():
    while True:
        print()
        print('[1] Ejercicio 1')
        print('[2] Ejercicio 2')
        print('[3] Ejercicio 3')
        print('[0] Salir')

        opcion = input('Ingrese su Opción [0-3]')
        valores_opcion = ['0','1','2','3']

        if opcion in valores_opcion:
            if opcion == '1':
                saludo = saludo_cordial()
                print(saludo)
            elif opcion == '2':
                saludo_personal()
            elif opcion == '3':
                numero_factorial()
            elif opcion == '0':
                print('Saliendo del sistema...')
                break
        else:
            print('Opción ingresada NO corresponde...')

menu_principal()

