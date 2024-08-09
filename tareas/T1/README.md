#  Tarea 1: DCCiudad 🚈🐈


## Consideraciones generales :octocat:

<Descripción sobre la construcción del código y sus alcances>

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Flujo del programa PT1 : Automatización (40pts) (66,7%)

##### Función informacion_red (2pts) ✅: Hecha completa

##### Función agregar_tunel (2pts) ✅ : Hecha completa

##### Función invertir tunel (3pts) ✅ : Hecha completa 

##### Función nivel_conexiones (4pts) ✅ : Hecha completa

##### Función rutas_posibles (4pts) ✅ : Hecha completa

##### Función ciclo_mas_corto (4pts) ✅: Hecha completa

##### Función estaciones_intermedias (4pts) ✅: Hecha completa

##### Función estaciones_intermedias_avanzado (4pts) ✅: Hecha completa

##### Función cambiar_planos (2pts) ✅: Hecha completa

##### Función asegurar_ruta (8pts) 🟠 : No tiene implementado revisar si se pueden quitar algunos túneles según su efecto en la ruta pedida, por lo que no entrega la lista vacia cuando debe. Tampoco elimina bien todos los túneles que debería por problemas en la iteración y sus condiciones. No se establece bien cuándo seguir iterando y cuándo no. 


#### Menú: 13 pts (21,7%)
##### ✅ Consola (5pts) : Hecha completa
##### ✅ Menú de Acciones (8pts) : Hecho completo
##### ✅ Modularización
##### ✅ PEP8



## Ejecución :computer:
El módulo principal de la tarea a ejecutar es red.py para el flujo particular de las funciones (PARTE 1 :Automatización) y main.py para el menú interactivo. Además se deben tener los siguientes archivos y directorios adicionales:
1. dcciudad.pyc en T1 
2. data (carpeta) en T1

Luego en el directorio principal debe estar "main.py" , "red.py", "dcciudad.pyc" y la carpeta con archivos txt "data". 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. Librería estándar python :```os```: ```función listdir()```, ```path``` 
2. Librería estándar python : ```sys```: ```argv```, ```exit()``` 

Ninguna de las librerias debe ser instalada 

### Librerías propias
No fueron usadas clases externas a las entregadas, pero si se creo la función menu () que tenía la iteración de interacción con el usuario dentro del archivo main.py. Como argumento recibe (red: any, nombre_estacion: str, nombre_red: str).


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:


1. En el menú se crea la función menú pero las revisiones previas se realizan en la validación de la entrega inicial en la consola, debido a que se asume que no se entrega el menú a menos que todo sea válido
2. En el menú se asume que cualquier otro ingreso diferente de las opciones dadas (1,2,3,4), es causal de término del programa.
3. La función menú no la consideré como una libreria en si misma, pero la explique como función propia
4. Asumí que podía utilizar un try-except justificado (value e index error) porque la función asegurar ruta da error en algunas situaciones, entonces en esos casos instauré volver al menú para no cortar el programa. 
5. Como dice el enunciado se asume que en la opción 3 se entrega una estación existente y un número positivo de estaciones intermedias. 
6. Debido a que no se aclaraba agregué al gitignore el archivo pycache debido a que no es de relevancia ni ayuda, en el entendimiento y\o ejecucción del programa. También se ignoró ejemplo.py, ya que no cumple ningún rol en el flujo de los programas y tampoco contiene librerías/módulos que se importaran en otros archivos.


-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://es.stackoverflow.com/questions/213125/existe-una-manera-simple-de-convertir-una-lista-de-tipo-str-a-una-de-tipo-int>: Este hace la conversión de todos los elementos tipo string de la lista que contiene los valores de la red. Usa en una sola linea la iteración de un for para pasar de str a int. Está implementado en el archivo <red.py> en la línea 169.
2. \<https://www.delftstack.com/es/howto/python/python-split-list-into-chunks/>: Este hace la división de una lista en partes iguales, dadas por un valor en específico. En este caso, debido a que las matrices de red son cuadradas es que el número de estaciones nos entrega el valor para la división de los elementos. Además esta fragmentación se realiza de forma condensada en una línea con una iteración de for, con slicing cíclico de [posición actual : posicion actual + longitud del corte].Está implementado en el archivo <red.py> en la línea 171. 
3. \<https://youtu.be/ZBx7oWCJ4aY?si=ozq-r1QxvFEtFIw5> : Se usó como guía para entender y aprender el objetivo de un menú interactivo. El menú utiliza un while true para hacer un loop donde se hay if-elif-else para comprobar casos. Está implementado en el archivo <main.py> en la línea 13. 
4. \<https://www.freecodecamp.org/espanol/news/sentencias-try-y-except-de-python-como-menejar-excepciones-en-python/> : Se uso para el try except, que permite conocer como capturar errores específicos. Está implementado en el archivo <main.py> en las líneas 38, 47 y 51.
