print("trabajando con listas,\n==================")
lista = ["Armando casas", True, 1.73]
print(lista)

print(type(lista))

print(lista[0])
print(lista[1])
print(lista[2])

print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))

nombre = str(input("Ingrese su nombre: "))
lista[0] = nombre #con esto se cambia el valor del elemento 0 en este caso de la lista
print(lista[0])
print(f"{lista}\n")

float_edad = float(input("Ingrese su edad: "))
lista[2] = float_edad
print(lista[2])
print(F"{lista}\n")

print("Trabajando con diccionarios \n=======")
diccionario = {
    "nombre_personal" : "armando casas",
    "esta emocionado" : True,
    "Altura" : 1.73
}

print(type(diccionario))
print(diccionario)
print(diccionario["nombre_personal"])

diccionario["nombre_personal"] = nombre #cambio en el valor
print(diccionario["nombre_personal"])

print("Trabajando con conjuntos\n============")
conjunto = {"Armando casas", True, 1.73}
print(type(conjunto))

conjunto.add(nombre)
conjunto.add(nombre) #No se puede repetir un valor ya agregado,asi que no se agrega nuevamente
print(f"{conjunto}")

print("Trabajando con tuplas \n=======")
tupla = ("Armando casas",True,1.73)
print(tupla)
print(type(tupla))
print(f"{tupla[0]}\n")