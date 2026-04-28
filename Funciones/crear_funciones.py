# Dentro del lenguaje,tenemos la opción de crear nuestras PROPIAS funciones
# para eso usamos la palabra reservada DEF

def suma(num_1,num_2):
    #Este sera el contenido de la función
    resultado = num_1 + num_2
    print(resultado,)

def resta(num_1,num_2):
    resultado = num_1 - num_2
    print(resultado)

def mult(num_1,num_2):
    resultado = num_1 * num_2
    print(resultado)

def div(num_1,num_2):
     if num_1  == 0:
        print("No se puede dividir en 0")
     elif num_2 == 0:
         print("No se puede dividir en 0")
     else:
         resultado = num_1 / num_2
         print(resultado)
      

num_1 = input('Ingrese el primer número: ')
num_2 = input('Ingrese el segundo número: ')

if num_1.isdigit() and num_2.isdigit():
    num_1 = float (num_1)
    num_2 = float (num_2)
suma(num_1,num_2)
resta(12,8)
mult(4,9)
div(10,2)