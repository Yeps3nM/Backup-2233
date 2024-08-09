import dcciudad
from os import listdir

class RedMetro:
    def __init__(self, red: list, estaciones: list) -> None:
        self.red = red
        self.estaciones = estaciones

    def informacion_red(self) -> list:
        """

        """
        cantidad_estaciones = len(self.estaciones) 
        cantidad_conexiones = [] 
        for estacion in self.red: 
            suma = 0
            for conexion_estacion in estacion: 
                suma += int(conexion_estacion) 
            cantidad_conexiones.append(suma)
        return [cantidad_estaciones,cantidad_conexiones]
    
    def agregar_tunel(self, inicio: str, destino: str) -> int:
        fila_inicio = self.estaciones.index(inicio)
        columna_destino = self.estaciones.index(destino) 
        # Verifica si no exiten túneles allí
        if int(self.red[fila_inicio][columna_destino]) == 0:          
            self.red[fila_inicio][columna_destino] += 1 
            total_tuneles = 0  
            for tunel in self.red[fila_inicio]: 
                total_tuneles += int(tunel) 
            return total_tuneles
        # Verifica si ya existen túneles allí
        elif int(self.red[fila_inicio][columna_destino]) != 0: 
            return -1
        
    def tapar_tunel(self, inicio: str, destino: str) -> int:
        fila_inicio = self.estaciones.index(inicio) 
        columna_destino = self.estaciones.index(destino) 
        #Ya existe túnel en esa posición
        if int(self.red[fila_inicio][columna_destino]) > 0 :        
            self.red[fila_inicio][columna_destino] -= 1         
            total_tuneles = 0 #Contador 
            for tunel in self.red[fila_inicio]: 
                total_tuneles += int(tunel)  
            return total_tuneles
        # No existe túnel en esa posición
        elif int(self.red[fila_inicio][columna_destino]) == 0 :      
            return -1
        
    def invertir_tunel(self, estacion_1: str, estacion_2: str) -> bool:
        posicion_estacion_1 = self.estaciones.index(estacion_1) 
        posicion_estacion_2 = self.estaciones.index(estacion_2) 
        #Valor en la el recorrido Estación_1 -> Estación_2
        posicion_est1_est2 = self.red[posicion_estacion_1][posicion_estacion_2] 
        #Valor en la el recorrido Estación_2 -> Estación_1
        posicion_est2_est1 = self.red[posicion_estacion_2][posicion_estacion_1] 
        #Existe ruta de E1->E2 y de E2->E1
        if posicion_est1_est2 == 1 and posicion_est2_est1 ==  1 : 
            return True
        #Existe ruta de E1->E2 pero no de E2->E1, se borra túnel de E1->E2, se agrega túnel de E2->E1
        elif posicion_est1_est2 == 1 and posicion_est2_est1 == 0 : 
            self.red[posicion_estacion_1][posicion_estacion_2] -= 1 
            self.red[posicion_estacion_2][posicion_estacion_1] += 1 
            return True
        #No existe ruta de E1->E2 pero si de E2->E1, se agrega túnel de E1->E2, se borra túnel de E2->E1
        elif posicion_est1_est2 == 0 and posicion_est2_est1 != 0 : 
            self.red[posicion_estacion_1][posicion_estacion_2] += 1 
            self.red[posicion_estacion_2][posicion_estacion_1] -= 1 
            return True 
        #No existe ruta de E1->E2 y tampoco de E2->E1
        elif posicion_est1_est2 == 0 and posicion_est2_est1 == 0 : 
            return False  
             
    def nivel_conexiones(self, inicio: str, destino: str) -> str:
        posicion_estacion_1 = self.estaciones.index(inicio) 
        posicion_estacion_2 = self.estaciones.index(destino) 
        posicion_est1_est2 = self.red[posicion_estacion_1][posicion_estacion_2]
        posicion_ant_est1_est2 = self.red[posicion_estacion_1][(posicion_estacion_2)-1]  
        #Existe ruta ciclica directa E1->E2
        if posicion_est1_est2 != 0 : 
            return "túnel directo"
        #No existe ruta directa de E1->E2 pero hay intermedia
        elif posicion_estacion_1 == 0 and posicion_ant_est1_est2 != 0: 
            return "estación intermedia"
        #Hay ruta entre E1 y E2 pero no hay intermedia
        elif dcciudad.alcanzable(self.red, posicion_estacion_1, posicion_estacion_2) == True and posicion_ant_est1_est2 == 0 : 
            return "muy lejos"
        #No hay ruta 
        elif dcciudad.alcanzable(self.red, posicion_estacion_1, posicion_estacion_2) == False : 
            return "no hay ruta" 
        
    def rutas_posibles(self, inicio: str, destino: str, p_intermedias: int) -> int: 
        posicion_estacion_1 = self.estaciones.index(inicio) 
        posicion_estacion_2 = self.estaciones.index(destino) 
        red_elevada = dcciudad.elevar_matriz(self.red, p_intermedias + 1) 
        #Hay ruta para esa cantidad de estaciones intermedias
        if red_elevada[posicion_estacion_1][posicion_estacion_2] != 0 : 
            return red_elevada[posicion_estacion_1][posicion_estacion_2]
        #No hay ruta, en matriz elevada la posición almacena 0
        else: 
            return 0
        
    def ciclo_mas_corto(self, estacion: str) -> int:
        posicion_estacion= self.estaciones.index(estacion)
        exponente_actual = 1 
        #Revisa ruta directa de X -> X
        if self.red[posicion_estacion][posicion_estacion] != 0: 
            return 0
        #Revisa con elevar matriz la siguiente menor cantidad de túneles
        else: 
            for i in range (len(self.red)): 
                red_elevada = dcciudad.elevar_matriz(self.red,exponente_actual)
                if red_elevada[posicion_estacion][posicion_estacion] != 0 : 
                    return exponente_actual-1
                else :
                    exponente_actual += 1 
            #No se encontró ruta dentro de la iteración 
            return -1 

    def estaciones_intermedias(self, inicio: str, destino: str) -> list:
        posicion_inicio= self.estaciones.index(inicio) 
        posicion_destino = self.estaciones.index(destino) 
        lista_redes = []
        numero_estacion_actual = 0 
        for estacion in self.red[posicion_inicio]: 
            #Revisamos que esa estación intermedia llegue a la final
            if estacion == 1 and self.red[numero_estacion_actual][posicion_destino] == 1 : 
                lista_redes.append(self.estaciones[numero_estacion_actual]) 
                numero_estacion_actual += 1  
            else : 
                numero_estacion_actual += 1 
        return lista_redes
    
    def estaciones_intermedias_avanzado(self, inicio: str, destino: str) -> list:
        posicion_inicio = self.estaciones.index(inicio) 
        posicion_destino = self.estaciones.index(destino) 
        lista_redes = []  
        estacion_actual = 0 
        for estacion in self.red[posicion_inicio]: 
            #Si el valor es 1 (hay ruta posible) (primera estación intermedia)
            if estacion == 1: 
                subestacion_actual = 0 
                #Se accede a la lista de la estación que tenía ruta existente
                for subestacion in self.red[estacion_actual]: 
                    #Si en esta sublista hay estaciones con ruta se revisa que estas tengan ruta con el destino final (segunda estación intermedia)
                    if subestacion == 1 and self.red[subestacion_actual][posicion_destino] == 1: 
                        lista_redes.append([self.estaciones[estacion_actual],self.estaciones[subestacion_actual]]) 
                    subestacion_actual += 1 
            estacion_actual += 1 
        return lista_redes
    
    def cambiar_planos(self, nombre_archivo: str) -> bool:
        lista_info_txt = []
        #Lista con todos los directorios en el file "data"
        lista_dir = listdir("data") 
        if nombre_archivo not in lista_dir :
            return False 
        else :
            with open ("data/"+ nombre_archivo, "r", encoding = "utf-8") as archivo: 
                for linea in archivo : 
                    linea = linea.strip() 
                    lista_info_txt.append(linea)  
            self.estaciones =  (lista_info_txt[1:int(lista_info_txt[0])+1]) 
            #Slicing sobre la cantidad de estaciones, que es primera posición de lista
            tamano_red = int(lista_info_txt[0]) 
            #Se transforma a lista, cortando por las comas el string que representa la red
            lista_red = lista_info_txt[-1].split(",") 
            #Se itera en la lista que tiene la red para transformar cada elemento a un entero numérico 
            intlist_red = [int(x) for x in lista_red] 
            #Itera y hace una lista de lista con elementos del tamaño de la red
            self.red = [intlist_red [numero: numero + tamano_red] for numero in range(0, len(intlist_red), tamano_red)]
            return True 
        
    def asegurar_ruta(self, inicio: str, destino: str, p_intermedias: int) -> list:
        posicion_inicio = self.estaciones.index(inicio) 
        posicion_destino = self.estaciones.index(destino) 
        red_elevada = dcciudad.elevar_matriz(self.red, int(p_intermedias + 1))  
        red_copia = self.red  
        #No hay ruta con esa cantidad de estaciones intermedias
        if red_elevada[posicion_inicio][posicion_destino] == 0 :
            return []
        # La cantidad para elevar supera la dimension de la red 
        elif p_intermedias > len(self.red): 
            return []
        else : 
            estacion_actual = 0 
            # Contador de túneles por pasar respecto a las estaciones intermedias
            cantidad_tuneles = p_intermedias + 1 
            if cantidad_tuneles != 0: 
                for estacion in self.red[posicion_inicio]: 
                    matriz_elevada = dcciudad.elevar_matriz(self.red, cantidad_tuneles) 
                    #Hay ruta y la matriz elevada a los túneles muestra que hay ruta para la cantidad faltante
                    if estacion == 1 and matriz_elevada[estacion_actual][posicion_destino] != 0 :
                        cantidad_tuneles -= 1
                    #Hay ruta pero la matriz elevada a los túneles muestra que no hay ruta para la cantidad faltante
                    elif estacion == 1 and matriz_elevada[estacion_actual][posicion_destino] == 0 :
                        red_copia[posicion_inicio][estacion_actual] == 0
                estacion_actual += 1 
        return red_copia
