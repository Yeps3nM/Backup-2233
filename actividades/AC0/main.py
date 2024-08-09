from entities import Item, Usuario
from utils.pretty_print import print_usuario, print_items,print_canasta

path_relativo = 'utils/items.dcc'

def cargar_items() -> list:
    items = []
    with open(path_relativo,'r') as archivo: 
        for linea in archivo : 
            linea = linea.strip().split(',')
            instancia_item = Item(linea[0], int(linea[1]), int(linea[2]))
            items.append(instancia_item)
    return items 

def crear_usuario(tiene_suscripcion: bool) -> Usuario:
    usuario = Usuario(tiene_suscripcion)
    print_usuario(usuario)
    return usuario

if __name__ == "__main__":
    # 1) Crear usuario (con o sin suscripcion)
    nuevo_usuario = crear_usuario(True)
    # 2) Cargar los items
    items_cargar = cargar_items()
    # 3) Imprimir todos los items usando los módulos de pretty_print
    print_items(items_cargar)
    # 4) Agregar todos los items a la canasta del usuario
    for e in items_cargar:
        nuevo_usuario.agregar_item(e)
    # 5) Imprimir la canasta del usuario usando los módulos de pretty_print
    print_canasta(nuevo_usuario)
    # 6) Generar la compra desde el usuario
    nuevo_usuario.comprar()
    # 7) Imprimir el usuario usando los módulos de pretty_print
    print_usuario(nuevo_usuario)
    


            
