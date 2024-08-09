from dcciudad import imprimir_red
import sys 
from os import path, listdir
from red import RedMetro

def menu( red: any, nombre_estacion: str, nombre_red: str) : 
    '''
    Esta función usa un while true para permitir una constante interacción con el usuario, se usan if-elif-else
    para cada una de las 4 opciones y una extra por si hay entradas no definidas. Se utiliza en el elif de la opción
    3 un try-except de index y value error para no cortar el programa, debido a que el método asegurar ruta está incompleto 
    y luego levanta errores en el método imprimir_red.
    '''
    while True: 
        print (f"""
        ¡Se cargó la red {nombre_red}
        La estación elegida es: {nombre_estacion}
        *** Menú de Acciones ***
        [1] Mostrar red
        [2] Encontrar ciclo más corto
        [3] Asegurar ruta
        [4] Salir del programa
        """)
        respuesta = int(input("Indique su opción (1, 2, 3 o 4):")) #Respuesta usuario

        if respuesta == 1: #Mostrar red 
            imprimir_red(red_ofc_consola.red, red_ofc_consola.estaciones)
            menu(red_ofc_consola.red, nombre_estacion, nombre_red)

        elif respuesta == 2: #Encontrar ciclo más corto
            ciclo_corto = red_ofc_consola.ciclo_mas_corto(nombre_estacion)
            if ciclo_corto == -1: #Si no hay ciclo más corto
                print ("Lo lamentamos el resultado es -1, no existe forma de llegar a la misma estación")
            else:  #Existe un ciclo más corto
                print(f"La cantidad mínima de estaciones intermedias es {ciclo_corto}")
            menu(red_ofc_consola.red, nombre_estacion, nombre_red) #Se continua loop while en cualquier caso

        elif respuesta == 3: #Asegurar red 
            try:
                #Se le pide al usuario ingresar cantidad de estaciones intermedias y el destino 
                estaciones_intermedias = int(input("Ingrese un número de estaciones intermedias por las que desea pasar"))
                estacion_destino  = input("Ingrese el nombre de la estación de destino") 
                #Se llama al método asegurar red con los datos solcitados y la estación inicio encontrada con argv 
                red_asegurada = red_ofc_consola.asegurar_ruta(nombre_estacion, estacion_destino, estaciones_intermedias)
                print(red_asegurada)
                imprimir_red(red_asegurada, red_ofc_consola.estaciones) #Se imprime nueva red 
                menu(red_ofc_consola.red, nombre_estacion, nombre_red) #Se continua loop while
            except ValueError: 
                print("¡Perdón! No se entregó la respuesta correctamente")
                print("Te redigiremos al menú porque todavía estamos trabajando en ese método")
                menu(red_ofc_consola.red, nombre_estacion, nombre_red) #Se continua loop while
            except IndexError: 
                print("¡Perdón! No se entregó la respuesta correctamente")
                print("Te redigiremos al menú porque todavía estamos trabajando en ese método")
                menu(red_ofc_consola.red, nombre_estacion, nombre_red) #Se continua loop while

        elif respuesta == 4: #Salir del programa
            sys.exit("Ha salido del programa. ¡Gracias por consultar!")

        else: #Cualquier otra opción, no válida termina el programa
            sys.exit("Error, no se ingresó una opción válida")

if __name__ == "__main__":
    #Genera lista con los argumentos de la consola
    argumentos_consola = sys.argv 
    
    #Validación cantidad de argumentos
    if len(argumentos_consola) != 3: 
        sys.exit("Error, se entregaron menos de 3 argumentos")
    
    #Lista con los archivos dentro de la carpeta data    
    lista_directorios = listdir("data")
    # Variable con slice de la red de la lista con argumetos de consola
    nombre_red= sys.argv[1] + ".txt" #Nombre red
    
    #Validaciones nombre red 
    if nombre_red not in lista_directorios:
            sys.exit("Error, la red ingresada no existe dentro de la carpeta data")
   
    # Variable con slice de la estacion de la lista con argumetos de consola
    nombre_estacion = sys.argv[2]
    #Obtención de la ruta, el nombre de estación con slicing de la lista
    ruta_archivo = path.join("data", nombre_red)
    lista_info_file_txt = []
    
    #Se abre archivo para obtener toda la información (estaciones y red)
    with open (ruta_archivo, "r", encoding = "utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip() #Cortar saltos de linea, espacios extremos
            lista_info_file_txt.append(linea) # Se agrega linea a la lista vaica
    
    #Variable que contiene slice de estaciones de la lista con las lineas de todo el archivo
    estaciones = (lista_info_file_txt[1:int(lista_info_file_txt[0])+1])
    #Slice primer elemento en la lista
    tamano_red = int(lista_info_file_txt[0]) 
    #Slice del último elemento en lista
    lista_red = lista_info_file_txt[-1].split(",")  
    #Se crea las variables de la red como lista de lista
    intlist_red = [int(x) for x in lista_red] # Transforma a int los valores str de la red 
    #Crea la lista de listas para que tenga las dimensiones dadas desde el archivo
    red = [intlist_red [numero: numero + tamano_red] for numero in range(0, len(intlist_red), tamano_red)]
    #Se intancia un objeto del tipo RedMetro para accedera los métodos en el menú
    red_ofc_consola = RedMetro(red, estaciones) 
    
    #Validaciones sobre la existencia de lo argumentos en los directorios
    if nombre_estacion not in estaciones:
        sys.exit(f"Error, la estación ingresada no existe dentro del archivo {nombre_red}")
    if nombre_red in lista_directorios and nombre_estacion in estaciones:
        menu(red_ofc_consola, nombre_estacion, nombre_red)
    else: 
        sys.exit("Error, hay algo fuera de lo normal revisa la existencia de los argumentos")
