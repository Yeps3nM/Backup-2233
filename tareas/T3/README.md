# Tarea 3: DCCervel :school_satchel:


## Consideraciones generales :octocat:

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:

- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores


#### Carga de datos: 2 pts (1%)
##### Función cargar_datos() ✅: Completa. Permite leer los archivos dependiendo del tamaño entregado, según el tipo de objeto identificado en la posición inicial de la línea leída, hace yield según la namedtuple que corresponda.

#### Consultas : 144pts (99%)  
##### Función animales_según_edad() 3pts ✅:
Según el operador entregado, se utilizan if para hacer filter sobre la edad entregada por los elementos generados. Luego se hace un map sobre esta misma para obtener solo el nombre. Se retorna un objeto map
##### Función animales_que_votaron_por() 3pts ✅:
Se aplica un filter sobre el generador de votos, que compara si el atirbuto de id candidato es igual al buscado.
##### Función cantidad_votos_candidato() 3pts ✅:
Se hace un filter sobre los votos generados que contenga solo al candidato pedido, luego se hace un map sobre el id del animal votante y se entrega la longitud de la lista por comprensión que formó el map.
##### Función ciudades_distritos() 3pts ✅:
Se realiza un map que obtiene solo las provincias desde el generador de distritos, luego se utiliza la función auxiliar lista_unica_gen que realiza un set por comprensión y una lista por comprensión que comprueba con lo contenido en el set. Se hace un map sobre si mismo para obtener un objeto map.
##### Función especies_postulantes() 6pts ✅:
Se utiliza counter para obtener el total por especies diferentes en generador de candidatos. Luego se hace una lista por comprensión que verifique si ese total cumple con ser mayor o igual al ingresado.
##### Función pares_candidatos() 6pts ✅:
Se hace un map sobre los nombres del generador de candidatos, porteriormente se realiza la combinatoria de tuplas de largo dos con estos nombres y se genera un objeto map con estas tuplas. Entregando las combinaciones de candidatos posibles.
##### Función votos_alcalde_en_local() 3pts ✅:
Se realiza un filter para solo tener aquellos locales que igualen al entregado y sobre aquello se hace un filter para tener solo al candidato solicitado.
##### Función locales_mas_votos_comuna() 6pts ✅:
Se hace un filtro por comuna para tener solo los generados que correspondan a la ingresada, luego se hace un filtro para saber que tiene un mínimo de votantes y se entrega un objeto map con la id del local.
##### Función votos_candidato_mas_votado() 6pts ✅:
Con el diccionario por comprensión del generador de votos y el counter de la repetión de los id.candidato desde el diccionario. Se calculá el máximo de votos obtenidos del total con la función most.common. Con un diccionario por comprensión que permite solo ingresar key-value que cumplan con el máximo de votos en su valor, se utiliza un reduce para identificar el id (key) más grande de entre los que tienen valor igual. Para entregar un filter con los id de votos que correspondan al candidato más votado.
##### Función animales_según_edad_humana() 6pts ✅:
Se hace un diccionario con la especie y su ponderador, luefo según el comparador se hacen ifs que permiten hacen un filter sobre aquellos elementos del generador de animales que multiplicando la edad por el ponderador correspondiente cumpliría lo solicitado.
##### Función animal_mas_viejo_edad_humana() 7pts ✅:
Se crea un diccionario por comprensión que contiene las especies con sus ponderadores, luego una lista que contiene todos los elementos del generador, a partir de esta lista se crean dos diccionario que guardan (id : edad ponderada) y (id: nombre). Luego se hace un reduce de los valores de la edad para conocer el mayor, desde la lista se filtra los que tienen la misma edad y con map se retornan solo los nombres de estos.
##### Función voto_por_especie() 7pts ✅:
Realiza un diccionario por id de candidato y especie con el generador de candidatos, para con el counter de votos de cada cantidado, realizar una lista de tuplas por comprensión que contengan la (especie, votos). Después de ordenan estas tuplas por especie, y se agrupan por lo mismo. Para posteriormente crear otra lista de tuplas pero que sume aquellas que tienen el mismo primer elemento.
##### Función hallar_region() 3pts ✅:
Filtra locales para encontrar id pedido, se encuentra el id de la comuna,del local respectivo y se obtiene el número enlistando por comprensión. Se utiliza el filtro sobre el generador de distritos para encontrar el de la comuna. Se mapea la región y se enlista. Retorna un str.
##### Función max_locales_distrito() 6pts ✅:
Se hace un counter por repeticion de comunas en el generador de locales, se realiza un diccionario que mantiene esa cuenta, luego con los distritos se hace una cuenta según su repetición por cantidad de comunas mencionadas y se saca el elemento más alto. Solo funciona con los test que no usan los datos de data.
##### Función votaron_por_si_mismos() 6pts ✅:
Identificar aquellos candidatos que votaron por si mismos, se filtra para hacer un match de id entre voto y candidato, se hacen los pares y se filtra nuevamente para que coincidan los ids. Se hace un map para obtener el nombre
            
##### Función ganadores_por_distrito() 7pts ❌:
##### Función mismo_mes_candidato() 7pts 🟠: Se filtra por votos del candidato mencionado, se hace un striptime cuando se contruye el diccionario con el id del animal y su fecha de nacimiento. Luego se ve la existencia del candidato. Se filtra si existiera.
No funciona en todos los test case, solo en algunos 
##### Función edad_promedio_humana_voto_comuna() 6pts ❌:
##### Función votos_iterespecie() 7pts ✅:
Retorna un generador con instancias de animales que votaron por candidatos de su misma especie o diferente, dependiendo del valor de misma_especie. Con diccionarios por cada generador (votos y candidato) que relacionan ambos los id del candidato, se usan ifs para saber el valor del bool, y luego saber filtrar aquellos votos que tengan el id del animal para tener los que efectivamente votaron. Luego aquello se filtra para saber si son o no de la misma especie dependiendo del valor bool.
##### Función porcentaje_apoyo_especie() 9pts ❌:
##### Función votos_validos() 6pts ✅:
Se hacen diccionarios por cada generador donde se pueda agregar en el del generador de animales la nueva edad por el ponderador correspondiente. Luego se filtran las edades nuevas según si son o no mayor o igual a 18 años.Posteriormente se hace una lista por comprensión con estos resultados y se entrega la longitud de esta misma.
##### Función cantidad_votos_especie_entre_edades() 6pts ❌:
##### Función distrito_mas_votos_especie_bisiesto() 7pts ❌:
##### Función votos_validos_local() 7pts ✅: Se utiliza el mismo código de validar por edad, luego se hace una lista con las intancias de Voto que tiene +18, se hace filter según si pertenecen a la comuna esperada y finalmente se devuelve un map con los id de aquellos votos validados.
##### Función votantes_validos_por_distritos() 8pts ❌:



El módulo principal de la tarea a ejecutar es  ```consultas.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```auxiliar.py``` en ```T3```
2. ```data``` en ```T3```
3. ```utilidades.py```en ```T3```

Por lo tanto, en el directorio principal debe estar "consultas.py", "auxiliar.py" y la carpeta con archivos csv "data" contiene sub carpetas : "l", "m" y "s". Todas con sus 6 archivos csv correspondientes: "animales.csv", "candidatos.csv", "distritos.csv", "locales.csv", "ponderadores.csv", "votos.csv".

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. Módulo ```typing```: ```Generator```

(Es una forma de dar hints sobre los tipos de datos que debe retornar en este caso las funciones)

2. Módulo ```collections```: ```namedtuple```, ```Counter```.

(Permite crear subclases de tuplas, y Counter permite obtener una subclase de dict que cuenta objetos hasheables)

3. Librería estándar python :```os```: ```path```
(Permite manejar las rutas, para poder estandarizarlas)

4. Módulo ```itertools```: ```combinations```, ```product```, ```groupby```.

(Retorna tuplas de un largo n, sin repecticiones, product entrega el producto cartesiano entre dos objetos y groupby permite agrupar elementos bajo una condición común)

5. Módulo ```functools```: ```reduce```.

(Permite aplicar una función continuamente sobre los elementos de un iterable)

6. Módulo ```datetime```: ```datetime```:```strptime```

(Convertir str a fechas establecidas)




### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```auxiliar```: Contiene  ```lista_gen```, ```lista_unica_gen``` y ```generador``` (Son funciones que permiten crear listas, sets y generadores por comprensión)

2. ```utilidades```: Contiene ```Animales```, ```Candidatos```,```Distritos```, ```Locales```, ```Votos``` y ```Ponderador```
 Hecha para determinar las namedtuples que generan los distintos tipos de generadores.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list>: este\<convierte una lista representada en strings a una lista > y está implementado en el archivo <consultas.py> en las líneas <48> y convierte el string en el que se enlistaban los ids de votantes a un objeto de tipo lista. 
2. \<https://www.pythonforbeginners.com/basics/generator-comprehension-in-python>:\<Hacer  generadores por comprensión> y está implementado en el archivo <auxiliar.py> en la línea <25> y convierte el iterador entregado en una generador (por comprensión).
3. \<https://www.geeksforgeeks.org/python-program-to-find-smallest-number-in-a-list/>: este <usa reduce para encontrar el valor mínimo en una lista> y está implementado en el archivo <consultas.py> en la línea <142, 178> y encuentra el valor máximo entre las llaves de un diccionario (se repite su uso con values en vez de keys).
4. \<https://www.w3resource.com/python-exercises/extended-data-types/python-extended-data-types-index-counter-exercise-8.php>: este <crea diccionarios por compresión con la condición de que los valores sean menor a un parámetro dado> y está implementado en el archivo <consultas.py> en la línea <139-141> y crea un diccionario por comprensión que solo deja aquellos key:values que tengan valores iguales al máximo de votos encontrado.
5. \<https://stackoverflow.com/questions/48606406/find-most-frequent-value-in-python-dictionary-value-with-maximum-count> : este <utiliza la función most_common() sobre los valores de un diccionario para encontrar solo 1 y entregar el valor y la llave correspondientes> y está implementado en el archivo <consultas.py> en la línea <138> donde da 1 uno de los elementos con mayor valor del counter, pero entrega solamente el número, no la llave asociada.
6.\<https://www.geeksforgeeks.org/python-get-sum-of-tuples-having-same-first-value/> : este <ordena las tuplas por el elemento en común, las agrupa por el mismo y luego con una lista por comprensión suma el valor de la segunda componente> y está implementado en el archivo <consultas.py> en la línea <189-191> cumple exactamente el mismo rol solo que con tuplas de especies y votos.
7. Para utilizar las funciones como combinations, Counter y product se leyó la documentación de python desde \<docs.python.org/>