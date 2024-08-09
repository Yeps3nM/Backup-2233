import entidades
import parametros

class Combate ():
    def ronda (ejercito_propio, enemigos):
        """
        Se toma copian ambos ejercitos luego se itera sobre los dos, se checkea que los combatientes
        actuales tengan vida, se guarda el daño calculado por atacar para cada uno, se hace remove si uno muere
        se resta al jugador y a su enemigo respectivamente. Si el enemigo se queda sin ejercito, se remueve
        de su lista original y se retorna 1. En caso de perder se retorna 0. Se revisa la condición
        del len dentro del while y fuera del while
        """
        ronda_enemigo = enemigos[0].copy()
        #CASO BASE se pelea con ejercito vacío
        if len(ejercito_propio) == 0:
            print("Tú perdiste")
            print("Vuelves a iniciar con un ejercito vacio!!")
            return (0)   
        for gato in ejercito_propio:
            for enemigo in ronda_enemigo:
                if len(ronda_enemigo) == 0 : #Enemigo queda sin combatientes
                    print("tú ganaste") 
                    print(enemigos)
                    return(1)
                elif len(ejercito_propio) == 0: #Nos quedamos sin combatientes
                    print("Tú perdiste")
                    print("Vuelves a iniciar con un ejercito vacio!!")
                    return (0)
                while gato._vida > 0 and enemigo._vida > 0 and len(ronda_enemigo) != 0 and len(ejercito_propio) != 0:
                    print(f"Ahora combate tu {gato.nombre} vs el enemigo {enemigo.nombre}")
                    daño_jugador = gato.atacar(enemigo) #Calculo daño
                    daño_enemigo = enemigo.atacar(gato) #Calculo daño
                    print(f"Estos son los daños {daño_jugador} y {daño_enemigo}")
                    gato.vida -= daño_enemigo #Bajamos stats
                    enemigo.vida -= daño_jugador
                    if gato._vida == 0 : #Muere un aliado
                        ejercito_propio.remove(gato)
                        print("Tu gato se quedó sin vida")
                    if enemigo._vida == 0: #Muere un enemigo
                        ronda_enemigo.remove(enemigo)
                        print("Enemigo con uno menos")
                    if len(ronda_enemigo) == 0 : #Enemigo queda sin combatientes
                        print("tú ganaste") 
                        print(enemigos)
                        return(1)
                    if len(ejercito_propio) == 0: #Nos quedamos sin combatientes
                        print("Tú perdiste")
                        print("Vuelves a iniciar con un ejercito vacio!!")
                        return (0)
    
                    