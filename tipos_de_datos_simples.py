# Tipos de datos en python

print(type(5))
print(type(3.2))
print(type("hola"))
print(type(True))

numero_entero = 0
numero_decimal = 0.0
cadena_de_texto = "Buneas estimado"
valor_booleano = False

print("No mi primer mensaje en python")

print()
print(numero_entero)
print(type(numero_entero))

print()
print(numero_decimal)
print(type(numero_decimal))

print()
print(cadena_de_texto)
print(type(cadena_de_texto))

print()
print(valor_booleano)
print(type(valor_booleano))

valor_booleano = 5 > 3
print()
print(valor_booleano)
print(type(valor_booleano))

#Concatenación de cadenas de texto
saludo = "Buen dia master,¿me deposita 5 lucas?"
nombre = " Antonio necesita 5 lucas"
print()
print(saludo + nombre)

texto_de_una_linea_comillas_dobles = "texto de una linea"
texto_de_una_linea_comillas_simples = 'texto de una linea'

texto_de_mulriples_lineas_comillas_dobles = """
Linea 1 texto multiples con dobles comillas
Linea 2 texto multiples con dobles comillas
Linea 3 texto multiples con dobles comillas
Linea 4 texto multiples con dobles comillas
"""
texto_de_multiples_lineas_comillas_simples = '''
Linea 1 texto multiples con comillas simples
Linea 2 texto multiples con comillas simples
Linea 3 texto multiples con comillas simples
Linea 4 texto multiples con comillas simples
'''

print(texto_de_una_linea_comillas_dobles)
print(texto_de_una_linea_comillas_simples)
print(texto_de_mulriples_lineas_comillas_dobles)
print(texto_de_multiples_lineas_comillas_simples)