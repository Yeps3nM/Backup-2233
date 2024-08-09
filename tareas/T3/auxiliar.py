def lista_gen(generador):
    """
    Esta función recibe un generador, se crea una lista por compresión
    con sus elementos y se retorna
    """
    lista = [x for x in generador]
    return lista


def lista_unica_gen(generador):
    """
    Esta función recibe un generador, se crea un set por
    compresión y luego se crea una lista por comprensión
    con los elementos del set y se retorna
    """
    set_og = {x for x in generador}
    lista_og = [x for x in set_og]
    return lista_og


def generador(iterador_dado: iter):
    """
    Se entrega un iterable y se retorna un generador por comprensión
    """
    return (x for x in iterador_dado)
