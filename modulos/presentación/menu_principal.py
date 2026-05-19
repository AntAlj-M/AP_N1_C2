#from datos import datos_menu
from datos import version

titulo = 'Sistema Gestión Biblioteca'

def menu_principal():
    print(f'{titulo} {version}')
    print(f'{'=' + len(titulo)}{'=' + len(version)}')