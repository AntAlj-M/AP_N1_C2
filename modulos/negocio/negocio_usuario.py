from presentacion.solicitud_datos import solicitar_datos_usuario
from datos import listado_usuarios
from prettytable import PrettyTable

def procesar_usuario():
    Nombre, Correo, Telefono, Rut, Contraseña = solicitar_datos_usuario()
    nuevo_usuario ={
        'id': len(listado_usuarios) + 1,
        'Nombre':Nombre.title(),
        'Correo':Correo,
        'Telefono':Telefono,
        'Rut':Rut,
        'Contraseña':Contraseña
    }
    listado_usuarios.append(nuevo_usuario)
    return listado_usuarios

def crear_tabla_usuario():
    tabla_usuario = PrettyTable()
    tabla_usuario.field_names = ['N°','Nombre','Correo','Telefono','Rut','Contraseña']

    for usuario in listado_usuarios:
        tabla_usuario.add_row([usuario['id'],usuario['Nombre'],usuario['Correo'],usuario['Telefono'],usuario['Rut'],usuario['Contraseña']])
    
    return tabla_usuario

def buscar_usuario(titulo):
    for usuario in listado_usuarios:
        if usuario['Nombre'].lower() == titulo.lower():
            return usuario