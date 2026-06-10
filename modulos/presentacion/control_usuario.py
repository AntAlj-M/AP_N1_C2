from datos.data_almacenada.info_usuarios import listado_usuarios
from prettytable import PrettyTable
from negocio import procesar_usuario,crear_tabla_usuario,buscar_usuario
from presentacion.solicitud_datos import solicitar_dato,nuevos_datos_usuario


def agregar_usuario():
    titulo = '\nAgregar Usuario'
    print(titulo)
    print('=' * len(titulo))
    listar_usuario()

    print('\nIngrese los datos del libro:')
    procesar_usuario()

def listar_usuario():
    tabla_usuario = PrettyTable()

    titulo = '\nListado de usuario'
    print(titulo)
    print('=' * len(titulo))
    tabla_usuario = crear_tabla_usuario()
    print(tabla_usuario)

def modificar_usuario():
    titulo = '\nModificar Usuario'
    print(titulo)
    print('=' * len(titulo))
    nombre = solicitar_dato('Ingrese el nombre del usuario: ')
    usuario = buscar_usuario(nombre)
    print(f'\nDatos del Usuario\n{"=" * 15}')
    print(f'N°: {usuario['id']} \nNombre: {usuario['Nombre']} \nCorreo: {usuario['Correo']} \nTelefono: {usuario['Telefono']} \nRut: {usuario['Rut']} \nContraseña: {usuario['Contraseña']}')
    nuevo_Nombre, nuevo_Correo, nuevo_Telefono, nuevo_Rut, nueva_Contraseña = nuevos_datos_usuario()
    
    if nuevo_Nombre != '':
        usuario['Nombre'] = nuevo_Nombre
    if nuevo_Correo != '':
        usuario['Correo'] = nuevo_Correo
    if nuevo_Telefono != '':
        usuario['Telefono'] = nuevo_Telefono
    if nuevo_Rut != '':
        usuario['Rut'] = nuevo_Rut
    if nueva_Contraseña != '':
        usuario['Contraseña'] = nueva_Contraseña

    print(f'\nDatos del Libro\n{"=" * 15}')
    print(f'N°: {usuario['id']} \nNombre: {usuario['Nombre']} \nCorreo: {usuario['Correo']} \nTelefono: {usuario['Telefono']} \nRut: {usuario['Rut']} \nContraseña: {usuario['Contraseña']}')

def eliminar_usuario():
    titulo = '\nEliminar Libro'
    print(titulo)
    print('=' * len(titulo))