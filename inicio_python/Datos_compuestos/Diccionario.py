nombre = str(int("Ingrese su nombre"))
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