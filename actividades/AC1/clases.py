from abc import ABC, abstractmethod
import random


class Vehiculo(ABC):
    identificador = 0
    def __init__(self, rendimiento: int, marca: str, energia = 120, *args, **kwargs) -> None:
        self.rendimiento = rendimiento
        self.marca = marca
        self.energia = energia # Cantidad de litros o watts #default 120? 
        self.identificador = Vehiculo.identificador #fijarlo como el valor actual de la variable de clase Vehiculo.identificador
        Vehiculo.identificador += 1 #uego se le debe sumar 1 a la misma variable
    @property  
    def energia (self): #getter de energia
        return self._energia
    @energia.setter 
    def energia (self, valor):
        if valor <= 0 :
            self._energia = 0
        elif valor > 0:
            self._energia = valor
    @abstractmethod
    def recorrer (self, kilometros) -> None: #cuanto puede andar en km
        pass
    @property
    def autonomia (self) -> float: #  la cantidad de kilómetros que puede andar el vehículo
        return float(self._energia * self.rendimiento)

class AutoBencina (Vehiculo):
    def __init__(self, bencina_favorita, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bencina_favorita = bencina_favorita

    def recorrer(self, kilometros) -> None:
        if  kilometros < self.autonomia:
            kilometros = kilometros
        elif kilometros >= self.autonomia:
            kilometros = int(self.autonomia)
        gasto_viaje = int(kilometros//self.rendimiento)
        self._energia -= gasto_viaje
        return f"Anduve por {kilometros}Km y gaste {gasto_viaje}L de bencina"

class AutoElectrico(Vehiculo):
    def __init__(self, vida_util_bateria, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.vida_util_bateria = vida_util_bateria # años de vida util
    
    def recorrer(self, kilometros) -> None:
        if  kilometros < self.autonomia:
            kilometros = kilometros
        elif kilometros >= self.autonomia:
            kilometros = int(self.autonomia)
        gasto_viaje = int(kilometros//self.rendimiento)
        self._energia -= gasto_viaje
        return f"Anduve por {kilometros}Km y gaste {gasto_viaje}W de energia electrica"
class Camioneta(AutoBencina):
    def __init__(self, capacidad_maleta, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.capacidad_maleta = capacidad_maleta


class Telsa(AutoElectrico):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def recorrer(self, kilometros) -> None:
        mensaje = super().recorrer(kilometros)
        return mensaje + " de forma inteligente"
    
class FaitHibrido (AutoBencina, AutoElectrico):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(vida_util_bateria = 5,*args, **kwargs)

    def recorrer(self, kilometros) -> str:
        return AutoBencina.recorrer(self, kilometros/2)+" "+AutoElectrico.recorrer(self, kilometros/2)
                                      
                                      