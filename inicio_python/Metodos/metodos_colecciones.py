#Metodos para trabajar con listas

animales = ['Gato','perro','Vaca','Conejo','Ornitorrinco','Murcielago']
frutas = ['Durazno','Fresa','Mango','Melon']
numeros = [5,6,7,1,56,789,2]
#El método APPEND agrega elementos al final de la lista
print(animales)
nuevo_animal = input("Agregue un nuevo animal a la lisa")
animales.append(nuevo_animal.title())
print(animales)

print(len(animales))
#El metodo INSERT agrega un elmento en la posición indicada
otro_nuevo_animal = input('Agregue un nuevo anikal a la lista: ')
animales.insert(0,otro_nuevo_animal.title())
print(animales)

#El metodo EXTEND agrega varios elementos a una lista
animales.extend(['Oveja','Cerdo'])
print(animales)
#Se puede agregar una lista completa a otra lista
animales.extend(frutas)
print(animales)

#El metodo POP permite eliminar elementos de una lista
#POP sin argumentos elimina el ultimo elemto de la lista
animales.pop()
print(animales)
#POP con el argumento indice eliminapor su ubicación
animales.pop(2)
print(animales)
#El metodo REMOVE elimina un elemnto por su valor
animales.remove('Vaca')
print(animales)

#Ordenando listas
#Si las lista es de string se ordena alfabeticamente
animales.sort()
print(animales)
#Si indicamos REVERSE = True,se ordena de forma alfabeticamente decreciente
animales.sort(reverse=True)
print(animales)
#Si la lista es de NÚMEROS se ordena de forma creciente
numeros.sort()
numeros.sort(reverse=True)
print(numeros)
#Si indicamos REVERSE = True,se ordena de forma decreciente

#El metodo CLEAR limpia completamente la lista
animales.clear()
print(animales)