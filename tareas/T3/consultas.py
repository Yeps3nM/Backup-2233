from typing import Generator
import os
from datetime import datetime
from collections import Counter
from functools import reduce
from itertools import product, combinations, groupby
from auxiliar import lista_gen, lista_unica_gen, generador
from utilidades import (
    Animales, Candidatos, Distritos, Locales,
    Votos, Ponderador)


def cargar_datos(tipo_generator: str, tamano: str):
    """
    Función que genera la ruta del archivo según el tamaño dado, para
    buscarlo en data. Se abre el archivo, se lee desde la priemra linea
    con datos útiles. Según que tipo indique el primer elemento de la linea
    se hace un yield de esta que concuerde con la namedtuple de ese tipo.
    Se cambian los tipos de datos si fuera necesario.
    *Entrega generadores del tipo de cada namedtuple/tipo del archivo
    """
    generador_nombre = tipo_generator + ".csv"
    path = os.path.join("data", tamano, generador_nombre)
    with open(path, "r", encoding="latin-1") as archivo:
        file = archivo.readlines()[1:]
    for linea in file:
        if tipo_generator == "animales":
            id, nombre, especie, id_comuna, peso_kg, edad, fecha_nacimiento = linea.strip().split(",")
            yield Animales(
                int(id), nombre, especie, int(id_comuna),
                float(peso_kg), int(edad), fecha_nacimiento)
        elif tipo_generator == "candidatos":
            id_candidato, nombre, id_distrito_postulacion, especie = linea.strip().split(",")
            yield Candidatos(
                int(id_candidato), nombre, int(id_distrito_postulacion), especie)
        elif tipo_generator == "distritos":
            id_distrito, nombre, id_comuna, provincia, region = linea.strip().split(",")
            yield Distritos(
                int(id_distrito), nombre, int(id_comuna), provincia, region)
        elif tipo_generator == "locales":
            locales = linea.strip().split(",", 3)
            id_local = int(locales[0])
            id_comuna = int(locales[2])
            votantes = locales[3]
            if votantes == "[]":
                id_votantes = []
            else:
                id_votantes = list(map(int, votantes[1:-1].split(',')))
            yield Locales(
                id_local, locales[1], id_comuna,
                id_votantes)
        elif tipo_generator == "ponderadores":
            especie, ponderador = linea.strip().split(",")
            yield Ponderador(especie, float(ponderador))
        elif tipo_generator == "votos":
            id_voto, id_animal_votante, id_local, id_candidato = linea.strip().split(",")
            yield Votos(
                int(id_voto), int(id_animal_votante), int(id_local),
                int(id_candidato))


def animales_segun_edad(generador_animales: Generator,
                        comparador: str, edad: int) -> Generator:
    if comparador == "<":
        edad_filtro = filter(lambda x: x.edad < edad, generador_animales)
        mapeo_nombre = map(lambda x: x.nombre, edad_filtro)
    if comparador == ">":
        edad_filtro = filter(lambda x: x.edad > edad, generador_animales)
        mapeo_nombre = map(lambda x: x.nombre, edad_filtro)
    if comparador == "=":
        edad_filtro = filter(lambda x: x.edad == edad, generador_animales)
        mapeo_nombre = map(lambda x: x.nombre, edad_filtro)
    return mapeo_nombre


def animales_que_votaron_por(generador_votos: Generator,
                             id_candidato: int) -> Generator:
    voto_filtro = filter(
        lambda x: x.id_candidato == id_candidato,
        generador_votos)
    mapeo_nombre = map(lambda x: x.id_animal_votante, voto_filtro)
    return mapeo_nombre


def cantidad_votos_candidato(generador_votos: Generator,
                             id_candidato: int) -> int:
    filtro_votos = filter(
        lambda x: x.id_candidato == id_candidato,
        generador_votos)
    mapeo_nombre = map(lambda x: x.id_animal_votante, filtro_votos)
    lista_nombre = [x for x in mapeo_nombre]
    return len(lista_nombre)


def ciudades_distritos(generador_distritos: Generator) -> Generator:
    mapeo_nombre = map(lambda x: x.provincia, generador_distritos)
    provincias_unicas = lista_unica_gen(mapeo_nombre)
    gen_provincias = map(lambda x: x, provincias_unicas)
    return gen_provincias


def especies_postulantes(generador_candidatos: Generator,
                         postulantes: int) -> Generator:
    mapeo_especie = Counter(x.especie for x in generador_candidatos)
    lista = [x for x in mapeo_especie if mapeo_especie[x] >= postulantes]
    return lista


def pares_candidatos(generador_candidatos: Generator) -> Generator:
    mapeo_nombre = map(lambda x: x.nombre, generador_candidatos)
    permuta_candidato = combinations(mapeo_nombre, 2)
    mapeo_datos = map(lambda x: x, permuta_candidato)
    return mapeo_datos


def votos_alcalde_en_local(generador_votos: Generator, candidato: int,
                           local: int) -> Generator:
    # id candidato e id local
    filtro_local = filter(lambda x: x.id_local == local, generador_votos)
    fil_candidato = filter(lambda x: x.id_candidato == candidato, filtro_local)
    return fil_candidato


def locales_mas_votos_comuna(
        generador_locales: Generator,
        cantidad_minima_votantes: int,
        id_comuna: int) -> Generator:
    fil_comuna = filter(lambda x: x.id_comuna == id_comuna, generador_locales)
    fil_min = filter(lambda x: len(x.id_votantes) >=
                     cantidad_minima_votantes, fil_comuna)
    mapeo_id = map(lambda x: x.id_local, fil_min)
    return mapeo_id


def votos_candidato_mas_votado(generador_votos: Generator) -> Generator:
    dict_voto = {x.id_voto: x.id_candidato for x in generador_votos}
    counter_dict = Counter(dict_voto.values())
    max_cant = (counter_dict.most_common(1))[0][1]
    filt_count = {
        word: count for word,
        count in counter_dict.items() if count == max_cant}
    max_id = reduce(max, filt_count.keys())
    filtro_id = filter(
        lambda x: dict_voto[x] == max_id,
        dict_voto)
    return filtro_id


def animales_segun_edad_humana(
        generador_animales: Generator,
        generador_ponderadores: Generator,
        comparador: str,
        edad: int) -> Generator:
    dict_pond = {x.especie: x.ponderador for x in generador_ponderadores}
    if comparador == "<":
        filtro_edad = filter(lambda x: x.edad *
                             dict_pond[x.especie] < edad, generador_animales)
        mapeo_nombre = map(lambda x: x.nombre, filtro_edad)
    if comparador == ">":
        filtro_edad = filter(lambda x: x.edad *
                             dict_pond[x.especie] > edad, generador_animales)
        mapeo_nombre = map(lambda x: x.nombre, filtro_edad)
    if comparador == "=":
        filtro_edad = filter(lambda x: x.edad *
                             dict_pond[x.especie] == edad, generador_animales)
        mapeo_nombre = map(lambda x: x.nombre, filtro_edad)
    return mapeo_nombre


def animal_mas_viejo_edad_humana(
        generador_animales: Generator,
        generador_ponderadores: Generator) -> Generator:

    dict_pond = {x.especie: x.ponderador for x in generador_ponderadores}
    lista_animal = [x for x in generador_animales]
    dict_nombre = {x.id: x.nombre for x in lista_animal}
    dict_edad = {x.id: x.edad * dict_pond[x.especie] for x in lista_animal}
    max_edad = reduce(max, dict_edad.values())
    filtro_id = filter(lambda x: x.edad *
                       dict_pond[x.especie] == max_edad, lista_animal)
    mapeo_nombre = map(lambda x: x.nombre, filtro_id)
    return mapeo_nombre


def votos_por_especie(generador_candidatos: Generator,
                      generador_votos: Generator) -> Generator:
    dict_candt = {x.id_candidato: x.especie for x in generador_candidatos}
    cantidad_votos = Counter(x.id_candidato for x in generador_votos)
    tuplas = [(dict_candt[x], cantidad_votos[x]) for x in dict_candt]
    tuplas.sort(key=lambda x: x[0])
    groups = groupby(tuplas, lambda x: x[0])
    output = [(k, sum(v for _, v in group)) for k, group in groups]
    return output


def hallar_region(generador_distritos: Generator,
                  generador_locales: Generator, id_animal: int) -> str:
    filtro_local = filter(
        lambda x: id_animal in x.id_votantes,
        generador_locales)
    mapeo_comuna = map(lambda x: x.id_comuna, filtro_local)
    valor_comuna = [x for x in mapeo_comuna]
    filtro_dist = filter(
        lambda x: x.id_comuna == valor_comuna[0],
        generador_distritos)
    mapeo_region = map(lambda x: x.region, filtro_dist)
    str_region = [x for x in mapeo_region]
    return str_region[0]


def max_locales_distrito(generador_distritos: Generator,
                         generador_locales: Generator) -> Generator:

    locales = Counter([x.id_comuna for x in generador_locales])
    max_val = locales.most_common(1)[0][1]
    dict_sup = {x: count for x, count in locales.items() if count == max_val}
    filtro_sup = [
        x.nombre for x in generador_distritos if x.id_comuna in dict_sup.keys()]
    distrito = Counter([x for x in filtro_sup])
    max_val = distrito.most_common(1)[0][1]
    lista_distritos = [x for x in distrito if distrito[x] == max_val]
    return lista_distritos


def votaron_por_si_mismos(generador_candidatos: Generator,
                          generador_votos: Generator) -> Generator:
    votos_propios = filter(
        lambda x: x.id_animal_votante == x.id_candidato,
        generador_votos)
    pares = product(votos_propios, generador_candidatos)
    filter_candidatos = filter(
        lambda x: x[0].id_candidato == x[1].id_candidato, pares)
    mapeo_nombres = map(lambda x: x[1].nombre, filter_candidatos)
    return (generador(mapeo_nombres))


def ganadores_por_distrito(generador_candidatos: Generator,
                           generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


def mismo_mes_candidato(
        generador_animales: Generator,
        generador_candidatos: Generator,
        generador_votos: Generator,
        id_candidato: str) -> Generator:
    filtro_votos = filter(
        lambda x: x.id_candidato == id_candidato,
        generador_votos)
    lista_votos = [x for x in filtro_votos]
    if len(lista_votos) == 0:
        return filtro_votos
    dict_animal = {
        x.id: datetime.strptime(
            x.fecha_nacimiento,
            '%Y/%m') for x in generador_animales}
    edad_candidato = [dict_animal[x] for x in dict_animal if x == id_candidato]
    if len(edad_candidato) == 0:
        return edad_candidato
    else:
        filtro_mes = filter(
            lambda x: dict_animal[x].year == edad_candidato[0].year or dict_animal[x].month == edad_candidato[0].month,
            dict_animal)
        lista_id = [x for x in filtro_mes]
        return lista_id


def edad_promedio_humana_voto_comuna(
        generador_animales: Generator,
        generador_ponderadores: Generator,
        generador_votos: Generator,
        id_candidato: int,
        id_comuna: int) -> float:
    # COMPLETAR
    pass


def votos_interespecie(
    generador_animales: Generator,
    generador_votos: Generator,
    generador_candidatos: Generator,
    misma_especie: bool = False,
) -> Generator:
    dict_votos = {x.id_animal_votante: x.id_candidato for x in generador_votos}
    dict_candidatos = {x.id_candidato: x.especie for x in generador_candidatos}
    if misma_especie:
        flt_existe = filter(
            lambda x: x.id in dict_votos.keys(),
            generador_animales)
        flt_especie = filter(
            lambda x: dict_candidatos[dict_votos[x.id]] == x.especie, flt_existe)
        return flt_especie
    if not misma_especie:
        flt_existe = filter(
            lambda x: x.id in dict_votos.keys(),
            generador_animales)
        flt_especie = filter(
            lambda x: dict_candidatos[dict_votos[x.id]] != x.especie, flt_existe)
        return flt_especie


def porcentaje_apoyo_especie(
        generador_animales: Generator,
        generador_candidatos: Generator,
        generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


def votos_validos(generador_animales: Generator,
                  generador_votos: Generator, generador_ponderadores) -> int:
    dict_pond = {x.especie: x.ponderador for x in generador_ponderadores}
    dict_animales = {x.id: x.edad *
                     dict_pond[x.especie] for x in generador_animales}
    filtro_edad = filter(
        lambda x: dict_animales[x.id_animal_votante] >= 18, generador_votos)
    list_votantes = [x for x in filtro_edad]
    return len(list_votantes)


def cantidad_votos_especie_entre_edades(
        generador_animales: Generator,
        generador_votos: Generator,
        generador_ponderador: Generator,
        especie: str,
        edad_minima: int,
        edad_maxima: int) -> str:
    pass


def distrito_mas_votos_especie_bisiesto(
        generador_animales: Generator,
        generador_votos: Generator,
        generador_distritos: Generator,
        especie: str) -> str:
    pass


def votos_validos_local(
        generador_animales: Generator,
        generador_votos: Generator,
        generador_ponderadores: Generator,
        id_local: int) -> Generator:
    dict_pond = {x.especie: x.ponderador for x in generador_ponderadores}
    dict_animales = {x.id: x.edad *
                     dict_pond[x.especie] for x in generador_animales}
    filtro_edad = filter(
        lambda x: dict_animales[x.id_animal_votante] >= 18, generador_votos)
    lista_edad = [x for x in filtro_edad]
    filtro_local = filter(
        lambda x: x.id_local == id_local, lista_edad)
    mapeo_id = map(
        lambda x: x.id_voto, filtro_local)
    return mapeo_id


def votantes_validos_por_distritos(
        generador_animales: Generator,
        generador_distritos: Generator,
        generador_locales: Generator,
        generador_votos: Generator,
        generador_ponderadores: Generator) -> Generator:
    pass
