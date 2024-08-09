# Tarea 2: DCCombatientes 🐈⚔️



## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Programación Orientada a Objetos: 12 pts (10%)
##### 🟠 Definición de clases, herencia y *properties*
    Las clases creadas fueron: 

        1. 🟠 Combatiente (hereda ABC): es una clase abstracta que posee en su init todos los atributos básicos que tienen si o si todo tipo de combatiente. Los atributs vida, poder, defensa, agilidad y resistencia son properties para controlar que siempre sea dentro de los rangos establecidos. Atacar, str y evolucionar son métodos abtractos porque todos son necesarios para los diferentes combatientes pero depende de cada uno cómo se ejecutan. 
        FALTA : El método evolucionar 

        #### Herencia

        2. 🟠 Guerrero (hereda Combatiente): es una subclase de Combatiente, hereda el mismo constructor pero agrega el atributo tipo_gato y sobreescribe el método abstracto atacar para establecer que atributos varían. Aquí no hay activación de poderes. El str se sobreescribe, y se cambia en el string de presentación el tipo de gato.
        FALTA : El método evolucionar 

        3. 🟠 Caballero (hereda Combatiente): es una subclase de Combatiente, hereda el mismo contructor pero agrega el atributo tipo_gato y sobreescribe el método abstracto atacar, que mantiene como base el de guerrero pero además incluye con la librería random, función choice el azar de alcanzar la probabilidad de activar un poder. 
        FALTA : El método evolucionar 

        4. 🟠 Mago (hereda Combatiente): es una subclase de Combatiente, hereda el mismo constructor pero agrega el atributo tipo_gato y sobreescribe el método abstracto atacar. Nuevamente se mantien de base el atacar de Guerrero y la aplicación de la función del módulo random que se comprueba su cumplimiento con if. También se sobreescribe el método abstracto __str__ para el tipo específico de gato.
        FALTA : El método evolucionar e ignorar la resistencia del enemigo en el método atacar.

        #### Multiherencia

        5. ✅ Paladin (hereda Guerrero y Caballero): es una subclase que se forma combinando Guerrero y Caballero, hereda ambos constructores con super() y se agrega el tipo de gato. El método sobreescrito atacar depende del resultado de choices de la librería random que bajo la probabilidad dada por los parámetros fijos, permite ver si ataca como Guerrero o en su defecto como Caballero. 


        6. ✅ Mago_de_Batalla (hereda Guerrero y Mago):es una subclase que se forma combinando Guerrero y Mago, hereda ambos constructores con super() y se agrega el tipo de gato. El método sobreescrito atacar, depende del resultado de choices de la librería random que bajo la probabilidad dada por los parámetros fijos, que permite ver si ataca como Guerrero o en su defecto como Mago.

        7. ✅ Caballero_Arcano (hereda Caballero y Mago):es una subclase que se forma combinando Caballero y Mago, hereda ambos constructores con super() y se agrega el tipo de gato. El método sobreescrito atacar depende del resultado de choices de la librería random que bajo la probabilidad dada por los parámetros fijos, permite ver si ataca como Caballero o en su defecto como Mago.

        8. 🟠 Ejercito (Combate): es una subclase que hereda el método combate, además posee como atributo una lista de sus integrantes como instancias de Combatiente y guarda el oro que poseen (comienza incialmente con el valor fijo ORO_INICIAL del archivo paramentetros). Tiene sobreescrito el método abstracto __str__ donde recorriendo la lista de combatientes se hace piezas que guarda el string de presentanción en el formato deseado y luego retorna todo enlistado. Tiene el método añadir_combatiente que hace un append de lo que sería una instancia de clase de combatientes a la lista del ejercito. En el métod atacar se llama al del primer combatiente de la lista. 
        FALTA : Definir correctamente el método combatir 

        9.  ✅ Pergamino: Indica uno de los ítemes solo tiene un método __str__ que entrega el nombre del ítem.
        10. ✅ Lanza : Indica uno de los ítemes solo tiene un método __str__ que entrega el nombre del ítem.
        11. ✅ Armadura : Indica uno de los ítemes solo tiene un método __str__ que entrega el nombre del ítem.
        12. 🟠Combate : Es una clase creada en un archivo separado, donde se establece el flujo del combate, es heredada por la clase Ejercito que instancia para la ronda 1. Tiene problemas porque no termina cuando algún bando llega sin vida (si baja las stats por daño la primera vez que se llama el método), no se conoce quien es el ganador, no se entrega dinero por partida ganada, y no se reinicia el programa por ronda perdida, siempre se vuelve al menú de inicio como si se hubiese ganado. Se asumía que los gatos con vida cero pueden ser curados cuando haya dinero disponible. Tampoco hay cambio de ronda.
        



#### Preparación del programa: 10 pts (8%)
##### ✅ Inicio de la partida : Cuando se maneja con la librería sys los argumentos de la consola, estos se validan (si no cumple se finaliza el programa) en términos de ser vacíos, ser números, ser menos de los solicitados y existir en la carpeta de dificultades. Luego si existen se validan internamente los que serían los datos de los combatientes, finalmente se crea la instancia de ejercito con una lista de instancias combatiente.
##### Adicionalmente se lee el archivo de unidades.txt donde se validan los datos de los gatos, y se crean instancias dependiendo de que tipo sean y se agregan a una lista respectiva a esta clasificación. Luego se inicializa una instancia de Ejercito vacio (propio del jugador). Finalmente se crea una instancia de la clase Menu, donde se entrega : intancia Ejercito enemigo, instancia Ejercito propio, lista de instancias de gatos disponibles ; lista guerreros, lista magos, lista caballeros.
##### Se instancia también un ejercito vacío que corresponde al del jugador, luego se inicia el menu y se disponen las distintas opciones, mostrando además el ORO_INICIAl y la ronda 1 . 


#### Entidades: 56 pts (47%)
##### 🟠 Ejército : Como se mencionó previamente, tiene bien definido el constructor, comienza el ejercito con el oro inicial, hay una lista con los combatientes de cada ejercito. El métod str si está sobreescrito y permite la presentación de todos los integrantes (está diseñado para el ejercito propio solamente porque es para una lista no lista de listas).El método de añadir combatientes funciona correctamente.
##### OBS: El método combatir, se escribe en otro archivo por espacio (combate.py), no funciona en su totalidad,lamentablemente se tuvo que comprobar las mismas condiciones en más de un loop pero aún así no siempre es capaz de verificar correctamente cuando el usuario gana. En los casos en que logra verificar si gana o pierde correctamente, en el primero da el dinero correspondiente, aumenta la ronda y lleva al menú de inicio, y está actualizado el ejercito. Si se pierde, se lleva al menú de inicio nuevamente con la partida reiniciada (esto si funciona bien)
#### Como no siempre se capta la victoria, se vuelve al menú de inicio con el ejercito actualizado pero no así la ronda y el dinero.
#### El método si permite eliminar de la lista el ejercito enemigo derrotado.
##### 🟠 Combatientes: Se relacionan en base a multiherencia, la clase abstracta base es Combatientes, tiene los atributos compartidos y establece como property : vida, defensa, poder, agilidad y resistencia que tiene un rango específico donde son valores correctos. Está implementado el método curarse. Los métodos atacar, __str__, evolucionar son abstractos, porque su implementación varía según el tipo de combatiente. No está implementado el método evolucionar. 
##### En las subclases que heredan de Combatiente y las que heredan de estas subclases, tiene sobreescrito el método atacar, considerando fórmulas distintas de cálculo para el atáque. Todas menos guerrero cumplen con la existencia de la función choices del módulo random para obtener o no el cumplimiento de la probabilidad de activar un poder. En caso de que se cumpla se ataca básicamente y se adiciona el poder. En el caso contrario se sigue el ataque básico que tienen todos por el igual, la fórmula de guerrero.
#### Estas subclases no tienen implementada la evolución a sus subsubclases, no se efectúa la evolución pero si está la parte de descontar el dinero al oro actual.

##### ✅ Ítems : Son clases que en sí mismas solo poseen un método que es el __str__ donde entregan el nombre del ítem. 

#### Flujo del programa: 30 pts (25%)
##### 🟠 Menú de Inicio : Permite navegar por las distintas opciones, termina en caso de errores de ingreso y también solicitadamente. Permite ir al menú tienda, presenta al ejercito, salir del programa, y el combate lo llama pero con los vacios propios de este método. No siempre es capaz de actualizar la ronda, no siempre da el dinero si se gana la ronda, si se reinicia si se pierde el combate. 
##### 🟠 Menú Tienda : Se despliega, muestra el oro actual, la función volver al menú inicio funciona, también se controla si no hay inputs válidos.
##### Para las opciones de comprar gatos, estos se eligen aleatoriamente con la función choice dentro del tipo solicitado si y solo si tiene dinero disponible y la lista de gatos no está vacia. Por ende, después de comprar se elimina de la tienda este gato.
##### 🟠 Selección de gato : El menú si se activa solo si el jugador desde el menú tienda seleccionó un ítem. Teniendo que previamente existir uno o más combatientes aptos para recibirlo. Maneja correctamente que los ingresos de imput de selección de un gato sean los correctos. Imprime (con un salto de línea demás) todos los combatientes aptos en la pantalla. No permite hacer evolución del seleccionado pero si cobra al momento de seleccionar uno.
##### 🟠 Fin del Juego : Como no se implementa aseguradamente bien el combate. Si reinicia bien cuando se pierde. Pero a veces al pasar rondas no se indica la victoria explicitamente y no se cumple lo necesitado, por ende no siempre se suman rondas hasta la 3 para terminar el programa (pero se escribió en el código).
##### 🟠 Robustez : Si se abordan los errores en los imputs de los menus, también se valida el contenido de los archivos externos. No se manejan los problemas de la evolución porque no está implementada y en algunos casos combatir podría dar errores los cuales no aseguré.

#### Archivos: 12 pts (10%)
##### ✅ Archivos .txt : Se abren los distintos archivos txt con with open y se maneja en caso de que no cumplan los valores mínimos o hayan clasificaciones erradas. 
##### ✅ parametros.py : Este archivo contiene todos los valores estáticos que se utilizan tanto en entidades.py como main.py. Aquellos correspondientes a precios son extraídos del enunciado y el resto son elegidos arbitrariamente. Se utiliza como un módulo a exportar. Los valores existentes aquí son: precios, probabilidades por cada tipo, valores iniciales, parámetros de aumento/disminución de stats.

#### Otros: 
##### ✅ gitignore : Se ignora la carpeta data, el enunciado y el log.
##### ✅ pep8 : *Se hacen archivos separados por la cantidad de líneas

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```archivo.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```entidades.py``` en ```T2```
2. ```parametros``` en ```T2```
3. ```combate``` en ```T2```
4. ```data``` en ```T2```

Por lo tanto, en el directorio principal debe estar "main.py", "parametros.py", "combate.py", "entidades.py" y la carpeta con archivos txt "data" (contiene : "dificil.txt", "facil.txt", "intermedio.txt", "unidades.txt").

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. Librería estándar python: ```random```: ```choices() ``` 

(Se utiliza para ver si se cumple o no aleatoriamente la probabilidad de activar el poder en cada personaje de entidades)

2. Librería estándar python :```os```: ```función listdir()```, ```path``` 

(Permite acceder a los directorios como una lista y manejar las rutas de acceso a archivos, respectivamente)

3. Librería estándar python : ```sys```: ```argv```, ```exit()``` 

(Maneja como lista los argumentos de la consola como lista y permite también terminar la ejecución de un programa, respectivamente )

4. Librería estándar python (Collections): ```abc```: ```ABC```, ```abstractmethod```

(Permite establecer que clases hereden ABC y sean clasificadas como abstractas y también notar qué métodos son abtractos dentro de la clase)

Ninguna de las librerías debe ser instalada 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```entidades```: Contiene a las clases ```Combatiente```, ```Guerrero```, ```Caballero```,  ```Mago```, ```Paladin```, ```Mago_de_Batalla```, ```Caballero_Arcano```,```Ejercito```,```Pergamino```,```Lanza```,```Armadura```
2. ```parametros``` (contiene valores fijos)
3. ```combate```: Contien clase ```Combate```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Cuando hay modificaciones en atributos por activación de poder, son definitivas. 
2. En el caso de los ataques, si el daño realizado es menor a 1, se asume que hace 1 de daño. Debido a que por enunciado siempre es mayor o igual a 1.
3. Se supuso que las opciones del menú de inicio como comprar combatientes/ítemes y presentar ejercito son solo respecto del propio ejercito no el enemigo, pero que si las otras elecciones como atacar afectan al ejercito enemigo. 
4. Se asume que no se pueden comprar gatos repetidos en el menú tienda.
5. Se asume que los gatos con vida 0 no pueden ser curados y son eliminados del ejercito.
6. Se asume que si gana las 3 rondas, se termina el juego con un mensaje y se cierra el programa.
7. Se asume que se pueden poner prints extra para guiar el suceso del juego
8. Se asume que los combatientes enemigos de cada ronda son eliminados en su totalidad después de estas.



-------





## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://github.com/IIC2233/Yeps3nM-iic2233-2024-1/blob/main/Tareas/T1/main.py>: este hace \<lee los argumentos de la consola los revisa y hace revisión de errores, también se usa una función menú para hacerlo interactivo> y está implementado en el archivo <main.py> en las líneas <222 - 223, 17-18 > y hace <maneja los argumentos de la consola y hacer revisión de los errores básicos, también hay menues interactivos. Cambian variables desde la original y ahora hay clases que moldean los menús pero sigue practicamente el mismo modelo copiado de iteración y revisión >
2. \<https://stackoverflow.com/questions/48810749/put-a-loop-in-the-str-class-atribute>: este hace \<Hace que un método __str__ sobreescrito pueda retornar un string con salto de lineas que incluye la información de todo un diccionario> y está implementado en el archivo <entidades.py> en las líneas <242-246> y hace <Permite guardar en una lista en el formato de presentación de los combatientes cada línea con sus atributos incluídos y retorna con un join de salto de línea que permite mostrar cada presentación en un salto distinto, lo distinto es que aquí es una lista de listas y necesita un loop adicional para ingresar a las instancias>