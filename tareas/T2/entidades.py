from abc import ABC, abstractmethod
import parametros
from combate import Combate
from random import choices
 
class Combatiente (ABC):
    def __init__(self, nombre, vida_max, defensa, poder, agil, rest) -> None:
        self.nombre = nombre
        self.vida_max= vida_max
        self._vida = vida_max
        self._poder = poder
        self._defensa = defensa 
        self._agilidad = agil
        self._resistencia = rest
        self.ataque = round((self.poder + self.agilidad + self.resistencia)*((2*self._vida) / self.vida_max))
    @property
    def vida (self):
        return self._vida
    @vida.setter
    def vida (self,valor):
        """
        Verifica que los cambios al atributo de vida estén
        dentro de valores naturales y con tope de la vida máxima
        """
        if valor >= self.vida_max:
            self._vida = self.vida_max
        elif valor <= 0:
            self._vida = 0 
        else:
            self._vida = valor 
    @property 
    def poder (self):
        return self._poder
    @poder.setter
    def poder (self,valor):
        """
        Verifica que los cambios al atributo 
        de poder sean de 1 en adelante
        y con tope de la vida máxima (lo mismo para las sgtes properties)
        """
        if valor <= 1:
            self._poder = 1 
        else:
            self._poder = valor
    @property 
    def defensa (self):
        return self._defensa
    @defensa.setter
    def defensa (self,valor):
        if valor <= 1:
            self._defensa = 1 
        else:
            self._defensa = valor
    @property 
    def agilidad (self):
        return self._agilidad
    @agilidad.setter
    def agilidad (self,valor):
        if valor <= 1:
            self._agilidad = 1 
        else:
            self._agilidad = valor
    @property 
    def resistencia (self):
        return self._resistencia
    @resistencia.setter
    def resistencia (self,valor):
        if valor <= 1:
            self._resistencia = 1 
        else:
            self._resistencia = valor
    def curarse (self, valor):
        self.vida += valor
    @abstractmethod
    def atacar (self):
        pass
    @abstractmethod
    def __str__ (self):
        pass
    @abstractmethod 
    def evolucionar (self, item):
        """
        Se utiliza como método abstracto, la evoluación depende
        de la subclase a la que corresponda 
        """
        pass 
class Guerrero (Combatiente):
    tipo_gato = "Guerrero"
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def atacar(self, peleador):
        #Se calcula cuanto se resta a la agilidad según la equivalencia del porcentaje
        resto_cansacio = (self.agilidad * parametros.CANSANCIO) // 100
        daño = round(self.ataque - peleador.defensa) 
        if daño < 1:
            daño = 1
        self.agilidad -= resto_cansacio
        return daño 
    def __str__(self):
        mitad_str = f"¡Hola! Soy {self.nombre}, un Gato Guerrero con {self._vida} / {self.vida_max} de vida,"
        return f"{mitad_str} {self.ataque} de ataque y {self.defensa} de defensa."
    def evolucionar(self, item):
        pass
class Caballero (Combatiente):
    tipo_gato = "Caballero"
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
    def atacar (self,peleador):
        """
        Se establece el ataque básico de guerrero y 
        Con una lista y las ponderaciones de sus opciones se usa
        la función choices para la selección al azar de la activación del poder.
        Se calcula el porcentaje al que equivale CANSANCIO de la resistencia 
        para modificarlos (modelo general para los métodos atacar del archivo).
        """
        no_poder = 100 - parametros.PROB_CAB
        probabilidad_poder = choices(["poder", "no poder"], weights = [parametros.PROB_CAB, no_poder])
        daño = round(self.ataque - peleador.defensa)
        resto_cansacio = (self.resistencia * parametros.CANSANCIO) // 100
        daño_poder = 0
        if daño < 1:
            daño = 1 
        #Activación de poderes
        if probabilidad_poder == "poder":
            peleador.poder -= parametros.RED_CAB
            fraccion = self.ataque * (parametros.ATQ_CAB / 100)
            daño_poder = round(fraccion - peleador.defensa)  
        self.resistencia -= resto_cansacio
        return (daño + daño_poder)
    def __str__(self):
        mitad_str = f"¡Hola! Soy {self.nombre}, un Gato Caballero con {self._vida} / {self.vida_max} de vida,"
        return f"{mitad_str} {self.ataque} de ataque y {self.defensa} de defensa."
    def evolucionar(self, item):
        pass
class Mago (Combatiente):
    tipo_gato = "Mago"
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def atacar(self, peleador):
        no_poder = 100 - parametros.PROB_MAG
        probabilidad_poder = probabilidad_poder = choices(["poder", "no poder"], weights = [parametros.PROB_MAG, no_poder])
        daño = round(self.ataque - peleador.defensa)
        resto_cansacio = (self.resistencia * parametros.CANSANCIO) // 100
        resto_cansacio_agil = (self.agilidad * parametros.CANSANCIO) // 100
        daño_poder = 0
        if daño < 1:
            daño = 1
        if probabilidad_poder == "poder":
            peleador.poder -= parametros.RED
            fraccion = self.ataque * (parametros.ATQ_MAG / 100) - peleador.defensa
            daño_poder = fraccion * (100 - parametros.RED_MAG / 100)
        self.resistencia -= resto_cansacio
        self.agilidad -= resto_cansacio_agil
        return (daño + daño_poder)
    def __str__(self):
        mitad_str = f"¡Hola! Soy {self.nombre}, un Gato Guerrero con {self._vida} / {self.vida_max} de vida,"
        return f"{mitad_str} {self.ataque} de ataque y {self.defensa} de defensa."
    def evolucionar(self, item):
        pass
    
class Paladin (Guerrero, Caballero):
    tipo_gato = "Paladin"
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def atacar(self,peleador):
        no_poder = 100 - parametros.PROB_PAL
        probabilidad_poder = choices(["caballero", "guerrero"], weights = [parametros.PROB_PAL, no_poder])
        suma_resist = (self.resistencia * parametros.AUM_PAL) // 100
        daño = 0
        if probabilidad_poder == "caballero":
            daño = Caballero.atacar(self, peleador)
        else:
            daño = Guerrero.atacar(self, peleador)
        self.resistencia += suma_resist
        return daño        
class Mago_de_Batalla (Guerrero, Mago):
    tipo_gato = "Mago de Batalla"
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def atacar(self, peleador):
        no_poder = 100 - parametros.PROB_MDB
        probabilidad_poder = choices(["mago", "guerrero"], weights = [parametros.PROB_PAL, no_poder])
        suma_defend = (self.resistencia * parametros.DEF_MDB) // 100
        resto_cansancio = (self.agilidad * parametros.CANSANCIO) // 100
        daño = 0
        if probabilidad_poder == "caballero":
            daño = Caballero.atacar(self, peleador)
        else:
            daño = Guerrero.atacar(self, peleador)
        self.defensa += suma_defend
        self.agilidad -= resto_cansancio
        return daño
class Caballero_Arcano (Caballero, Mago):
    tipo_gato = "Caballero Arcano"
    def __init__(self,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def atacar(self, peleador):
        no_poder = 100 - parametros.PROB_CAR
        probabilidad_poder = choices(["caballero", "mago"], weights = [parametros.PROB_CAR, no_poder])
        suma_poder = (self.poder * parametros.AUM_CAR) // 100
        suma_agil = (self.agilidad * parametros.AUM_CAR) // 100
        resto_rest = (self.resistencia * parametros.CANSANCIO) // 100
        daño = 0
        if probabilidad_poder == "caballero":
            daño = Caballero.atacar(self, peleador)
        elif probabilidad_poder == "mago":
            daño = Mago.atacar(self, peleador)
        self.poder += suma_poder
        self.agilidad += suma_agil
        self.resistencia -= resto_rest
        return daño
#Clases ítemes 
class Pergamino :
    def __str__(self) -> str:
        return "Pergamino"
class Lanza :
    def __str__(self) -> str:
        return "Lanza"
class Armadura :
    def __str__(self) -> str:
        return "Armadura"

class Ejercito (Combate) :
    def __init__(self, *args, **kwargs) -> None:
        self.combatientes = []
        self.oro = parametros.ORO_INICIAL
    def combatir (self, ejercito_enemigo): 
        valor = Combate.ronda(self.combatientes, ejercito_enemigo)
        return valor #Retornamos al Menú el resultado
    def __str__(self) :
        """
        Lo que hace es que por cada instancia de un Combatiente (que son subelementos de la lista general) genera 
        una frase str con el formato que incluye los atributos,
        estos se almacenan en una lista y luego se hace un return uniendo cada una con un salto de linea cosa que
        se vean en la consola de forma consecutiva. En caso de que no haya ejercito se imprime un mensaje especial.
        """
        if len(self.combatientes) == 0:
            return f"¡Actualmente tu ejercito está vacio!"
        pieces = ["*** Este es tu Ejercito Actual ***"]
        frase = "¡Hola! soy {}, un Gato {} con {} / {} de vida, {} de ataque y {} de defensa"
        for cat in self.combatientes:
            pieces.append(frase.format(cat.nombre, cat.tipo_gato, cat._vida, cat.vida_max, cat.ataque, cat.defensa))
        return "\n".join(pieces)
    def añadir_combatiente (self,combatiente):
        self.combatientes.append(combatiente)
        