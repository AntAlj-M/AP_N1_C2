def solicitar_datos_libro():
    titulo_libro = isbn = editorial = paginas = categoria = ''
    while titulo_libro == '':
        titulo_libro = input('Título: ').strip()
    while isbn == '':
        isbn = input('ISBN: ').strip()
    while editorial == '':
        editorial = input('Editorial: ').strip()
    while paginas == '':
        paginas = input('Cantidad de Páginas: ').strip()
    while categoria == '':
        categoria = input('Categoría: ').strip()
    return titulo_libro,isbn,editorial,paginas,categoria

def solicitar_datos_usuario():
    Nombre = Correo = Telefono = Rut = Contraseña = ''
    while Nombre == '':
        Nombre = input('Nombre: ').strip()
    while Correo == '':
        Correo = input('Correo: ').strip()
    while Telefono == '':
        Telefono = input('Telefono: ').strip()
    while Rut == '':
        Rut = input('Rut: ').strip()
    while Contraseña == '':
        Contraseña = input('Contraseña: ').strip()
    return Nombre,Correo,Telefono,Rut,Contraseña


def solicitar_dato(mensaje_input):
    tipo_dato = ''
    while tipo_dato == '':
        tipo_dato = input(f'{mensaje_input}').strip()
        return tipo_dato

def nuevos_datos_libro():
    print('Ingrese los nuevos datos del libro o presione enter para no realizar cambios')
    nuevo_titulo = nuevo_isbn = nuevo_editorial = nuevas_paginas = nueva_categoria = ''

    nuevo_titulo = input('Nuevo Título: ').strip()
    nuevo_isbn = input('Nuevo ISBN: ').strip()
    nuevo_editorial = input('Nuevo Editorial: ').strip()
    nuevas_paginas = input('Nueva Cantidad de Páginas: ').strip()
    nueva_categoria = input('Nueva Categoría: ').strip()
    return nuevo_titulo,nuevo_isbn,nuevo_editorial,nuevas_paginas,nueva_categoria

def nuevos_datos_usuario():
    print('Ingrese los nuevos datos del usuario o presione enter para no realizar cambios')
    nuevo_Nombre = nuevo_Correo = nuevo_Telefono = nuevo_Rut = nueva_Contraseña = ''

    nuevo_Nombre = input('Nuevo Nombre: ').strip()
    nuevo_Correo = input('Nuevo Correo: ').strip()
    nuevo_Telefono = input('Nuevo Telefono: ').strip()
    nuevo_Rut = input('Nuevo Rut: ').strip()
    nueva_Contraseña = input('Nueva Contraseña: ').strip()
    return nuevo_Nombre,nuevo_Correo,nuevo_Telefono,nuevo_Rut,nueva_Contraseña