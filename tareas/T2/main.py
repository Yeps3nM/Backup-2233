from os import path, listdir
from sys import argv, exit
import parametros
from random import choice
import entidades as ent

    
class Menu  (ent.Ejercito):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
        self.ronda = 1
        self.ejercito = args[0]
        self.enemigo = args[1]
        self.gatos_guerreros = args[2]
        self.gatos_magos = args[3]
        self.gatos_caballero = args[4]
    def menu_inicio (self): 
        while True:
            print(f"""
            *** Menú de inicio ***
            Dinero disponible: {self.ejercito.oro}
            Ronda actual: {self.ronda}
            [1] Tienda
            [2] Ejercito
            [3] Combatir
            [0] Salir del programa
            Indique su opción: 
            """)
            usuario = (input("Indique cuál opción (1, 2, 3 o 0):"))
            if usuario.isalpha() == True: #Verifica que entregue algo numérico
                exit("Error no se ingresó un número")
            if usuario.isspace() == True or usuario == "": #Verifica que no sea argumento vacio
                exit("Error se entregó vacío")
            usuario = int(usuario)
            if usuario == 1: #Ir a la tienda
                self.menu_tienda()
            elif usuario == 2: #Ejercito 
                print(self.ejercito)
            elif usuario == 3: #Combate 
                """
                Se busca llamar al método combate del Ejercito, en caso de que 
                ganen y retorne 1, se suma el dinero. En el otro caso se reinicia el ejercito
                vacio y se vuelve a la ronda 1
                """
                valor = self.ejercito.combatir(self.enemigo.combatientes)
                if valor == 1: #Ganaste
                    self.ronda += 1 #Una ronda más
                    self.ejercito.oro += parametros.ORO_GANADO
                    self.enemigo.combatientes.pop(0)
                    print("Volviste victorioso del combate")
                    if self.ronda == 3:
                        exit("¡Ganaste! Venciste a todes")
                elif valor == 0: #Perdiste
                    print("Bienvenide a un juego nuevo!")
                    reinicio = ent.Ejercito()
                    self.ejercito = reinicio # se reinicia el ejercito
                    self.ronda = 1 #Vuelve a ronda inicial
            elif usuario == 0:
                exit("Has salido del programa. ¡Vuelve pronto a combatir!")
            else: #Errores distintos de los primeros 
                exit("Hay un error, no has ingresado una opción válida")

    def menu_tienda(self):
        """
        Se revisa que el oro actual permita comprar, 
        si es así en el caso de los gatos se usa el random choice
        para elegir uno, en el caso de los ítemes se revisa compatibilidad
        con el ejercito actual para la evolución
        """

        print(f"""
            *** Tienda ***

            Dinero disponible: {self.ejercito.oro}
            
                    Producto      Precio
            [1] Gato Mago           10
            [2] Gato Guerrero       10
            [3] Gato Caballero      10
            [4] Ítem Armadura       5
            [5] Ítem Pergamino      5
            [6] Ítem Lanza          5
            [7] Curar Ejército      7
            
            [0] Volver al Menú de inicio
            
            Indique su opción:
            """)
        usuario = (input("Indique cuál opción (1, 2, 3, 4, 5, 6, 7 o 0):"))
        if usuario.isalpha() == True:
            print("Error no se ingresó un número")
            self.menu_tienda()
        if usuario.isspace() == True or usuario == "":
            print ("Error se entregó vacío")
            self.menu_tienda()
        usuario = int(usuario)
        if usuario == 1:
            gatos_disp = len(self.gatos_magos)
            if self.ejercito.oro >= parametros.PRECIO_MAG and gatos_disp != 0:
                gato_nuevo = choice(self.gatos_magos)
                self.gatos_magos.remove(gato_nuevo)
                self.ejercito.añadir_combatiente(gato_nuevo) 
                self.ejercito.oro -= parametros.PRECIO_MAG 
                print("Tu nuevo combatiente es:")
                print(gato_nuevo)
                print("La compra ha sido un éxito")
            else: 
                print("Falló la transacción")
            self.menu_tienda()
        elif usuario == 2 :
            gatos_disp = len(self.gatos_guerreros)
            if self.ejercito.oro >= parametros.PRECIO_GUE and gatos_disp != 0:
                gato_nuevo = choice(self.gatos_guerreros)
                self.gatos_guerreros.remove(gato_nuevo)
                self.ejercito.añadir_combatiente(gato_nuevo) 
                self.ejercito.oro -= parametros.PRECIO_GUE
                print("Tu nuevo combatiente es:")
                print(gato_nuevo)
                print("La compra ha sido un éxito")
            else: 
                print("Falló la transacción")
            self.menu_tienda() 
        elif usuario == 3:
            gatos_disp = len(self.gatos_caballero)
            if self.ejercito.oro >= parametros.PRECIO_CAB and gatos_disp != 0:
                gato_nuevo = choice(self.gatos_caballero)
                self.gatos_caballero.remove(gato_nuevo)
                self.ejercito.añadir_combatiente(gato_nuevo) 
                self.ejercito.oro -= parametros.PRECIO_CAB 
                print("Tu nuevo combatiente es:")
                print(gato_nuevo)
                print("La compra ha sido un éxito")
            else: 
                print("Falló la transacción")
            self.menu_tienda()
        elif usuario == 4: #Armadura compatible Mago - Gue
            if self.ejercito.oro >= parametros.PRECIO_ARMADURA:
                compatibles = []
                for gato in self.ejercito.combatientes:
                    if gato.tipo_gato == "Mago" or gato.tipo_gato == "Guerrero":
                        compatibles.append(gato)
                if len(compatibles) > 0 :
                    self.menu_gatos(compatibles)
                    self.ejercito.oro -= parametros.PRECIO_ARMADURA   
                else:
                    print("Tu ejercito no tiene gatos compatibles con el ítem")
            else: 
                print("Falló la transacción")
            self.menu_tienda()
        elif usuario == 5: #Pergamino compatible Gue - Cab
            if self.ejercito.oro >= parametros.PRECIO_PERGAMINO:
                compatibles = []
                for gato in self.ejercito.combatientes:
                    if gato.tipo_gato == "Caballero" or gato.tipo_gato == "Guerrero":
                        compatibles.append(gato)
                if len(compatibles) > 0 :
                    self.menu_gatos(compatibles)
                    self.ejercito.oro -= parametros.PRECIO_PERGAMINO   
                else:
                    print("Tu ejercito no tiene gatos compatibles con el ítem")
            else: 
                print("Falló la transacción")
            self.menu_tienda()
        elif usuario == 6: # Lanza compatible Mag - Cab 
            if self.ejercito.oro >= parametros.PRECIO_LANZA:
                compatibles = []
                for gato in self.ejercito.combatientes:
                    if gato.tipo_gato == "Mago" or gato.tipo_gato == "Caballero":
                        compatibles.append(gato)
                if len(compatibles) > 0 :
                    self.menu_gatos(compatibles)
                    self.ejercito.oro -= parametros.PRECIO_LANZA  
                else:
                    print("Tu ejercito no tiene gatos compatibles con el ítem")
            else: 
                print("Falló la transacción")
            self.menu_tienda()
        elif usuario == 7:
            if self.ejercito.oro >= parametros.PRECIO_CURA:
                for cat in self.ejercito.combatientes:
                    cat.curarse(parametros.CURAR_VIDA)
                self.ejercito.oro -= parametros.PRECIO_CURA
                print("¡Tu ejército ha recuperado vida!")
            else: 
                print("Falló la transacción")
            self.menu_tienda()
        elif usuario == 0:
            self.menu_inicio() #revisar por herencia
        else:
            print("Error ingresaste una opción no válida")
            self.menu_tienda()

    def menu_gatos (self, compatibles):
        print("""
        *** Selecciona un gato ***
              
                Clase        Nombre
            """)
        #Para completar con los compatibles se hace un loop por los disponibles
        contador = 1
        for gato in compatibles:
            print(f""" 
            [{contador}] Gato {gato.tipo_gato}   {gato.nombre}
                  """)
            contador += 1 
        print("""
        Indique su opción:
              """)
        usuario = (input("Indique cuál opción :"))
        if usuario.isalpha() == True:
            print("Error no se ingresó un número")
            self.menu_tienda()
        if usuario.isspace() == True or usuario == "": 
            print ("Error se entregó vacío")
            self.menu_tienda()
        usuario = int(usuario)
        if usuario not in range(1, len(compatibles) + 1):
            print("¡¡No está ese gato como opción!!")
            self.menu_tienda()
if __name__ == "__main__":
    #Lista con argumentos de la consola
    argumentos_consola = argv 
    directorios_data = listdir("data")
    #Validación de los argumentos para la dificultad y la cantidad de argumentos
    if len(argumentos_consola) != 2 :
        exit("Error, se entregó un total distinto de 2 en argumentos")
    #Validar si no es una string vacio
    if argumentos_consola[1].isspace() == True:
        exit("Error, se entregó un argumento vacío")
    #Validar si es un string y no numeros
    if argumentos_consola[1].isalpha() == False :
        exit("Error, se entregó un número no una dificultad" )
    dificultad_juego = argumentos_consola[1] + ".txt"
    if dificultad_juego not in directorios_data: #Validación existencia de ese archivo
        exit("¡¡La dificultad seleccionda no es una opción válida!!")
    ruta_archivo = path.join("data", dificultad_juego)
    informacion_base_juego= []
    #Lectura archivo DIFICULTAD y validación de los atributos de cada combatiente
    with open (ruta_archivo, "r", encoding = "utf-8") as archivo:
        for linea in archivo:
            lista_ronda_ok = []
            lista_ronda1 = linea.strip().split(";")
            #La linea que tiene combatientes de una ronda se separa en cada uno
            for gato_str in lista_ronda1:
                atributos = gato_str.strip().split(",")
                nombre = str(atributos[0])
                vid_max = int(atributos[2])
                defend = int(atributos[3])
                poder = int(atributos[4])
                agil = int(atributos[5])
                resist = int(atributos[6])
                #Validar si los atributos son correctos en cuando a tipo y valores int
                if atributos[1] == "CAB":
                    if vid_max >= 0 and defend >= 1 and poder >= 1 and agil >= 1 and resist >= 1:
                        instancia_cab = ent.Caballero(nombre, vid_max, defend, poder, agil, resist)
                        lista_ronda_ok.append(instancia_cab)
                    else : 
                        exit("¡¡El archivo contiene valores nulos y/o negativos!!")
                elif atributos[1] == "MAG":
                    if vid_max >= 0 and defend >= 1 and poder >= 1 and agil >= 1 and resist >= 1:
                        instancia_mag = ent.Mago(nombre, vid_max, defend, poder, agil, resist)
                        lista_ronda_ok.append(instancia_mag)
                    else: 
                        exit("¡¡El archivo contiene valores nulos y/o negativos!!")
                elif atributos[1] == "GUE":
                    if vid_max >= 0 and defend >= 1 and poder >= 1 and agil >= 1 and resist >= 1:
                        instancia_gue = ent.Guerrero(nombre, vid_max, defend, poder, agil, resist)
                        lista_ronda_ok.append(instancia_gue)
                    else :
                        exit("¡¡El archivo contiene valores nulos y/o negativos!!")
                elif atributos[1] == "PAL":
                    if vid_max >= 0 and defend >= 1 and poder >= 1 and agil >= 1 and resist >= 1:
                        instancia_pal = ent.Paladin(nombre, vid_max, defend, poder, agil, resist)
                        lista_ronda_ok.append(instancia_pal)
                    else: 
                        exit("¡¡El archivo contiene valores nulos y/o negativos!!")
                elif atributos[1] == "CAR":
                    if vid_max >= 0 and defend >= 1 and poder >= 1 and agil >= 1 and resist >= 1:
                        instancia_car = ent.Caballero_Arcano(nombre, vid_max, defend, poder, agil, resist)
                        lista_ronda_ok.append(instancia_car)
                    else: 
                        exit("¡¡El archivo contiene valores nulos y/o negativos!!")
                elif atributos[1] == "MDB": 
                    if vid_max >= 0 and defend >= 1 and poder >= 1 and agil >= 1 and resist >= 1:
                        instancia_mdb = ent.Mago_de_Batalla(nombre, vid_max, defend, poder, agil, resist)
                        lista_ronda_ok.append(instancia_mdb)
                    else: 
                        exit("¡¡El archivo contiene valores nulos y/o negativos!!")
                else:
                    exit("¡¡El archivo contiene información errada sobre los combatientes!!")
            informacion_base_juego.append(lista_ronda_ok)
    #Lectura archivo Unidades y validación de los atributos de cada gato
    gatos_guerreros = []
    gatos_magos = []
    gatos_caballero = []
    with open ("data/unidades.txt", "r", encoding = "utf-8") as archivo:
        contador = 0
        for linea in archivo:
            lista = linea.strip().split(",")
            nombre = str(lista[0])
            vid_max = int(lista[2])
            defend = int(lista[3])
            poder = int(lista[4])
            agil = int(lista[5])
            resist = int(lista[6])
            if lista[1] == "GUE": 
                if vid_max >= 0 and defend >= 1 and poder >= 1 and agil >= 1 and resist >= 1:
                    nombre_actual = ent.Guerrero(nombre, vid_max, defend, poder, agil, resist)
                    gatos_guerreros.append(nombre_actual)
                else: 
                    exit("Error, hay valores inválidos en el archivo")
            elif lista[1] == "MAG":
                if vid_max >= 0 and defend >= 1 and poder >= 1 and agil >= 1 and resist >= 1:
                    nombre_actual = ent.Mago(nombre, vid_max, defend, poder, agil, resist)
                    gatos_magos.append(nombre_actual)
                else:
                    exit("Error, hay valores inválidos en el archivo")
            elif lista[1] == "CAB":
                if vid_max >= 0 and defend >= 1 and poder >= 1 and agil >= 1 and resist >= 1:
                    nombre_actual = ent.Caballero(nombre, vid_max, defend, poder, agil, resist)
                    gatos_caballero.append(nombre_actual)
                else: 
                    exit("Error, hay valores inválidos en el archivo")
            else:
                exit("¡Hay otra información de un gato no identificado!")
    ejercito_enemigo = ent.Ejercito()
    ejercito_enemigo.combatientes = informacion_base_juego
    ejercito_propio = ent.Ejercito()
    juego1 = Menu(ejercito_propio, ejercito_enemigo, gatos_guerreros, gatos_magos, gatos_caballero)
    juego1.menu_inicio()