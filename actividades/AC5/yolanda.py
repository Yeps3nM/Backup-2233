import api
import requests


class Yolanda:

    def __init__(self, host, port):
        self.base = f"http://{host}:{port}"
        self.regex_validador_fechas = ''  # TODO: Completar
        self.regex_extractor_signo = ''  # TODO: Completar

    def saludar(self) -> dict:
        respuesta = requests.get(f"{self.base}/")
        data = respuesta.json()
        return {"status-code": respuesta.status_code, "saludo": data["result"] }

    def verificar_horoscopo(self, signo: str) -> bool:
        respuesta = requests.get(f"{self.base}/signos")
        data = respuesta.json()
        if signo in data["result"] :
            return True
        else: 
            return False 

    def dar_horoscopo(self, signo: str) -> dict:
        respuesta = requests.get(f"{self.base}/horoscopo", params = {"signo": signo} )
        data = respuesta.json()
        return {"status-code": respuesta.status_code, "mensaje": data["result"]}

    def dar_horoscopo_aleatorio(self) -> dict:
        respuesta = requests.get(f"{self.base}/aleatorio")
        data = respuesta.json()
        if respuesta.status_code != 200:
            return {"status-code": respuesta.status_code, "mensaje": data["result"]}
        else:
            respuesta_dos = requests.get(f"{data['result']}")
            data_dos = respuesta_dos.json()
            return {"status-code":respuesta_dos.status_code, "mensaje": data_dos["result"]}

        return "Completar"
    #token acceso , incluir en request header dict 
    def agregar_horoscopo(self, signo: str, mensaje: str, access_token: str) -> str:
        my_headers = {"Authorization": access_token}
        data = {'signo': signo, 'mensaje': mensaje}
        respuesta = requests.post(f"{self.base}/update", headers= my_headers, data= data)
        datos = respuesta.json()
        if respuesta.status_code == 401:
            return "Agregar horóscopo no autorizado"
        elif respuesta.status_code == 400:
            return datos["result"]
        else :
            return "La base de YolandAPI ha sido actualizada"

    def actualizar_horoscopo(self, signo: str, mensaje: str, access_token: str) -> str:
        my_headers = {"Authorization": access_token}
        data = {'signo': signo, 'mensaje': mensaje}
        respuesta = requests.patch(f"{self.base}/update", headers= my_headers, data= data)
        datos = respuesta.json()
        if respuesta.status_code == 401:
            return "Editar horóscopo no autorizado"
        elif  respuesta.status_code == 400:
            return datos["result"]
        else: 
            return "La base de YolandAPI ha sido actualizada"

    def eliminar_signo(self, signo: str, access_token: str) -> str:
        my_headers = {"Authorization": access_token}
        data = {'signo': signo}
        respuesta = requests.delete(f"{self.base}/remove", headers= my_headers, data=data)
        datos = respuesta.json()
        if respuesta.status_code == 400:
            return datos["result"]
        elif respuesta.status_code == 401:
            return "Eliminar signo no autorizado"
        else: 
            return "La base de YolandAPI ha sido actualizada"


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 4444
    DATABASE = {
        "acuario": "Hoy será un hermoso día",
        "leo": "No salgas de casa.... te lo recomiendo",
    }
    thread = api.Server(HOST, PORT, DATABASE)
    thread.start()

    yolanda = Yolanda(HOST, PORT)
    print(yolanda.saludar())
    print(yolanda.dar_horoscopo_aleatorio())
    print(yolanda.verificar_horoscopo("acuario"))
    print(yolanda.verificar_horoscopo("pokemon"))
    print(yolanda.dar_horoscopo("acuario"))
    print(yolanda.dar_horoscopo("pokemon"))
    print(yolanda.agregar_horoscopo("a", "aaaaa", "pepaiic2233"))
    print(yolanda.dar_horoscopo("a"))
