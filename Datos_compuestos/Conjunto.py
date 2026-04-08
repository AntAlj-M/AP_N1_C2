nombre = str(int("Ingrese su nombre"))
print("Trabajando con conjuntos\n============")
conjunto = {"Armando casas", True, 1.73}
print(type(conjunto))

conjunto.add(nombre)
conjunto.add(nombre) #No se puede repetir un valor ya agregado,asi que no se agrega nuevamente
print(f"{conjunto}")