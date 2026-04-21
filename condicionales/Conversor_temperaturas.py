# Teniendo 3 escalas 

#escala = ""
#Temperatura = 0
#escala_deseada = 0

#Temperatura = input('Escriba la temperatura sin la escala')

#if Temperatura.isdigit():
    #Temperatura = float(Temperatura)
    #print(type(Temperatura))
#else:
    #print('Ingrese un dato valido')

#escala = input('Indique la escala\n1-Celcius \n2-Fahrenheit \n3-Kelvin \n')
#escala = int(escala)

#escala_deseada = input('A que escala desea convertir?\n 1-Celcius \n2-Fahrenheit \n3-Kelvin \n')
#escala_deseada = int(escala_deseada)

#if escala and escala_deseada > 3:
#    if escala == 1:
#        print("escala es 1")
#    elif escala == 2:
#        print("escala es 2")
#    elif escala == 3:
#        print("escala es igual a 3")
#else:
#    print("Ingrese un número de 1 al 3")




print('Sistema conversor de temperaturas')
print('=================================')
print('Para comenzar ingrese su escala ')
print('C - para Celcius')
print('F - para Farenheit')
print('K - para kelvin')

escala_inicial = input('Ingrese escala inicial: ').upper()
str_temperatura = input('Ingrese su temperatura: ')
escala_final = input('Ingrese escala final: ').upper()

if str_temperatura.isdigit():
    temperatura = float(str_temperatura)
else:
    print("El valor de temperatura NO corresponde")

if escala_inicial == "F":
    pass
elif escala_inicial == 'C':
    pass
elif escala_inicial == 'K':
    pass
else:
    print("Escala final No corresponde")

if escala_final == "F":
    pass
elif escala_final == 'C':
    pass
elif escala_final == 'K':
    pass
else:
    print("Escala final No corresponde")

print(resultado)