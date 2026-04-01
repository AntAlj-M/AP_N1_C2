#saludo = "Buen dia master,¿me deposita 5 lucas? "
#nombre = input("Ingrese su nombre: ")
#print()
#print(saludo + nombre)

#Ingrese 2 numeros mediante su teclado y muestre el resultado de la suma

saludos = "Soy una calculadora que solo sabe sumar,ingrese dos números que quiera sumar por favor:"
numero_1 = 0
numero_2 = 0
resultado = 0

print(saludos)

numero_1 = float(input("Ingrese el primer número: "))

numero_2 = float(input("Ingrese el segundo número: "))

resultado = numero_1 + numero_2

#convierto el resultado en str para concatenarlo con el mensaje
#print("el resultado de la suma es de: " + str(resultado))

#La F es para formatear la cedena,como un pc,y como se formatea se vuelve cadena de texto y las llaves nos permiten poner las variables dentro de un texto,por eso esta entre comillas
#print(F"el resultado de la suma es de:  {resultado}")
print(F"{numero_1} + {numero_2} = {resultado}")

