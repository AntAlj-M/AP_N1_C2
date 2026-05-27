from datos import listado_libros
from prettytable import PrettyTable
def agregar_libro():
    titulo = 'Agregar libro'
    print('Agregar Libro')
    print('titulo')
    print('-' * len(titulo))
    print('Ingrese los datos del libro:')
    titulo_libro,Isbn,editorial,paginas,categoria = solicitar_datos_libro()

def listar_libros():
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['Titulo','ISBN','Editorial','Páginas','Categoria']

    titulo = '\nListado libros'
    print(titulo)
    print('-' * len(titulo))
    for libro in listado_libros:
        tabla_libros.add_row([libro['titulo_libro'],libro['Isbn'],libro['editorial'],libro['paginas'],libro['categoria']])
    print(tabla_libros)

def modificar_libro():
    titulo = 'Modificar libro'
    print('Modificar Libro')
    print('Agregar Libro')
    print('titulo')
    print('-' * len(titulo))

def eliminar_libro():
    titulo = 'Eliminar_libro'
    print('Eliminar Libro')
    print('Agregar Libro')
    print('titulo')
    print('-' * len(titulo))
    
def solicitar_datos_libro():
    titulo_libro = input('Titulo: ')
    Isbn = input('Isbn: ')
    editorial = input('Editorial: ')
    paginas = input('cantidad de páginas: ')
    categoria = input('categoría: ')
    return titulo_libro,Isbn,editorial,paginas,categoria