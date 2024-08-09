from copy import copy
from collections import defaultdict
from functools import reduce
from itertools import product
from typing import Generator

from parametros import RUTA_PELICULAS, RUTA_GENEROS
from utilidades import (
    Pelicula, Genero, obtener_unicos, imprimir_peliculas,
    imprimir_generos, imprimir_peliculas_genero, imprimir_dccmax
)


# ----------------------------------------------------------------------------
# Parte 1: Cargar dataset
# ----------------------------------------------------------------------------

def cargar_peliculas(ruta: str) -> Generator:
    with open (ruta,"r") as file:
        archivo = file.readlines()[1:]
    for linea in archivo:
        id, titulo, director, año_estreno, rating_promedio = linea.strip().split(",")
        yield Pelicula(int(id), titulo, director, int(año_estreno), float(rating_promedio))
    #for the unpack https://stackoverflow.com/questions/36787768/naming-elements-in-python-list

def cargar_generos(ruta: str) -> Generator:
    with open (ruta,"r") as file:
        archivo = file.readlines()[1:]
    for linea in archivo:
        genero, id_pelicula = linea.strip().split(",")
        yield Genero(genero, int(id_pelicula))


# ----------------------------------------------------------------------------
# Parte 2: Consultas sobre generadores
# ----------------------------------------------------------------------------

def obtener_directores(generador_peliculas: Generator) -> set:
    direct_unit = map(lambda x: x.director, generador_peliculas)
    return obtener_unicos(direct_unit)


def obtener_str_titulos(generador_peliculas: Generator) -> str:
    titulos = map(lambda x: x.titulo, generador_peliculas)
    string = reduce(lambda x, y: x + ", " + y, titulos, "")
    #', The Great Gatsby' != 'The Great Gatsby'
    # linea del reduce : https://www.geeksforgeeks.org/python-concatenate-rear-elements-in-tuple-list/
    return string[2:]

def filtrar_peliculas(
    generador_peliculas: Generator,
    director: str | None = None,
    rating_min: float | None = None,
    rating_max: float | None = None
) -> filter:
    if director != None:
        filtro = filter(lambda x: x.director == director, generador_peliculas)
    if rating_min != None:
        filtro = filter(lambda x: x.rating >= rating_min, generador_peliculas)
    if rating_max != None:
        filtro = filter(lambda x: x.rating <= rating_max, generador_peliculas)
    return filtro

def filtrar_peliculas_por_genero(
    generador_peliculas: Generator,
    generador_generos: Generator,
    genero: str | None = None
) -> Generator:
    pares = product(generador_peliculas, generador_generos)
    pares_filtro = filter(lambda x: x[0].id_pelicula == x[1].id_pelicula, pares)
    if genero != None:
        pares_filtro = filter(lambda x: x[1].genero == genero, pares)
    return pares_filtro

# ----------------------------------------------------------------------------
# Parte 3: Iterables
# ----------------------------------------------------------------------------

class DCCMax:
    def __init__(self, peliculas: list) -> None:
        self.peliculas = peliculas

    def __iter__(self):
        return IteradorDCCMax(self.peliculas)


class IteradorDCCMax:
    def __init__(self, iterable_peliculas: list) -> None:
        self.peliculas = copy(iterable_peliculas)
        self.peliculas.sort(reverse= True, key=lambda x: x.rating)
        self.peliculas.sort(reverse = False, key = lambda x: x.estreno)
        #sort del otro lado con estreno primero dio malo
    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        if not self.peliculas :
            raise StopIteration()
        proxima = self.peliculas.pop(0)
        return proxima

if __name__ == '__main__':
    print('> Cargar películas:')
    imprimir_peliculas(cargar_peliculas(RUTA_PELICULAS))
    print()

    print('> Cargar géneros')
    imprimir_generos(cargar_generos(RUTA_GENEROS), 5)
    print()

    print('> Obtener directores:')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    print(list(obtener_directores(generador_peliculas)))
    print()

    print('> Obtener string títulos')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    print(obtener_str_titulos(generador_peliculas))
    print()

    print('> Filtrar películas (por director):')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(filtrar_peliculas(
        generador_peliculas, director='Christopher Nolan'
    ))
    print('\n> Filtrar películas (rating min):')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(filtrar_peliculas(generador_peliculas, rating_min=9.1))
    print('\n> Filtrar películas (rating max):')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(filtrar_peliculas(generador_peliculas, rating_max=8.7))
    print()

    print('> Filtrar películas por género')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    generador_generos = cargar_generos(RUTA_GENEROS)
    imprimir_peliculas_genero(filtrar_peliculas_por_genero(
        generador_peliculas, generador_generos, 'Biography'
    ))
    print()

    print('> DCC Max...')
    imprimir_dccmax(DCCMax(list(cargar_peliculas(RUTA_PELICULAS))))