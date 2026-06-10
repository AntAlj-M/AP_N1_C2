#str_edad = input("Ingrese su edad: ")
#edad = int(str_edad)

#Condicional if
#if edad >= 18:
    #Este set de acciones se ejecuta cuando la respuesta es V
    #print('Wena,podi tomar y ser demandado legalmente')
#else:
    #Este set de acciones se ejecuta cuando la respuesta es F
    #print('Aprovecha de flojear,si es que quieres')

#Solicite al usuario el ingreso de datos personales (nombre, edad y titulo)
#Si el usuario es mayor de edad, muestre por pantalla todos sus datos
#Si el usuario no es mayor de edad, muestre un mensaje indicando que es menor de edad

#nombre = input("Ingrese su nombre: ")
#edad_p = int(input("Ingrese su edad: "))
#titulo = input("Ingrese su titulo: ")

#if edad_p >= 18:
    #print(f'Sus datos son los siguientes \n Su nombre es : {nombre}\n Su edad es : {edad_p}\n Su titulo es : {titulo}')
#else:
    #print("Usted es menor de edad")

#Para evaluar varias condiciones suamos if con ELIF
str_sueldo_mensual = input('Ingrese su sueldo mensual: $')
sueldo_mensual = 0.0 #float(str_sueldo_mensual)

if str_sueldo_mensual.isdigit():
    sueldo_mensual = float(str_sueldo_mensual)
else:
    print('Valor ingresado No corresponde!')

if sueldo_mensual > 0:
    if sueldo_mensual >= 7000000:
        print('Ud,pertenece al grupo alta / elite')
    elif 3500000 < sueldo_mensual <= 7000000:
        print('Ud, pertenece al grupo clase alta profesional')
    elif 2000000 < sueldo_mensual <= 3500000:
        print('Ud, pertenece al grupo clase media alta')
    elif 1200000 < sueldo_mensual <= 2000000:
        print('Ud, pertenece al grupo media emergente')
    elif 700000 < sueldo_mensual <= 1200000:
        print('Ud,pertenece al grupo media baja')
    elif sueldo_mensual <= 700000:
        print('Ud,pertenece al grupo baja')
    else:
        print('Sueldo ingresado no corresponde...')
