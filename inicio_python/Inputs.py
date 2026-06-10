#Cada dato ingresado mediante input ES UN TEXTO

numero = input("Por favor,ingrese un numero entero...")
print(type(numero))
print(numero)

print(f"SU NUMERO MULTIPLICADO POR 2 ES : {numero * 4}") #multiplica el texto de manera literal
print(f"SU NUMERO (convertido a entero) MULTIPLICADO POR 2 ES : {int(numero) * 2}") #Se puede convertir un entero a decimal pero no un decimal con entero
print(f"SU NUMERO (convertido a decimal) MULTIPLICADO POR 2 ES : {float(numero) * 2}")