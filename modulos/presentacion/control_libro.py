from datos import listado_libros
from prettytable import PrettyTable
from negocio import procesar_libro,crear_tabla_libros,buscar_libro
from presentacion.solicitud_datos import solicitar_dato,nuevos_datos_libro

def agregar_libro():
    titulo = '\nAgregar Libro'
    print(titulo)
    print('=' * len(titulo))
    listar_libros()

    print('\nIngrese los datos del libro:')
    procesar_libro()

def listar_libros():
    tabla_libros = PrettyTable()

    titulo = '\nListado de Libros'
    print(titulo)
    print('=' * len(titulo))
    tabla_libros = crear_tabla_libros()
    print(tabla_libros)

def modificar_libro():
    titulo = '\nModificar Libro'
    print(titulo)
    print('=' * len(titulo))
    titulo_libro = solicitar_dato('Ingrese el título del libro: ')
    libro = buscar_libro(titulo_libro)
    print(f'\nDatos del Libro\n{"=" * 15}')
    print(f'N°: {libro['id']} \nTítulo: {libro['titulo_libro']} \nISBN: {libro['isbn']} \nEditorial: {libro['editorial']} \nCantidad Páginas: {libro['paginas']} \nCategoría: {libro['categoria']}')
    nuevo_titulo, nuevo_isbn, nuevo_editorial, nuevas_paginas, nueva_categoria = nuevos_datos_libro()
    
    if nuevo_titulo != '':
        libro['titulo_libro'] = nuevo_titulo
    if nuevo_isbn != '':
        libro['isbn'] = nuevo_isbn
    if nuevo_editorial != '':
        libro['editorial'] = nuevo_editorial
    if nuevas_paginas != '':
        libro['paginas'] = nuevas_paginas
    if nueva_categoria != '':
        libro['categoria'] = nueva_categoria

    print(f'\nDatos del Libro\n{"=" * 15}')
    print(f'N°: {libro['id']} \nTítulo: {libro['titulo_libro']} \nISBN: {libro['isbn']} \nEditorial: {libro['editorial']} \nCantidad Páginas: {libro['paginas']} \nCategoría: {libro['categoria']}')

def eliminar_libro():
    titulo = '\nEliminar Libro'
    print(titulo)
    print('=' * len(titulo))