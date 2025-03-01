import json
import requests
import sys


class Actividad_1():
    def __init__(self):
        self.ruta_static="src/static/"
        sys.stdout.reconfigure(encoding='utf-8')

    def leer_json(self):
        # r read w write

        #ruta_json = "{}json/datos_persona.json".format(self.ruta_static)
        ruta_json=""
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = json.load(f)
            return datos 
        
    #escribir json    
    def escribir_json(self,ruta,data):
        
        ruta_json = "{}json/js.json".format(self.ruta_static)
        datos=""
        with open(ruta,'w',) as f:
            json.dump(data, f, indent=4)
        
    #leer api       
    def leer_api(self, url):
        # El get()método envía una solicitud de GET a la url especificada.
        response = requests.get(url)
        return response.json()
    
    
    
    #def escribir_txt(self,nombre_archivo="",datos=object):
    def escribir_txt(self,nombre_archivo="",datos=None): # "" '' """ """
        if nombre_archivo=="":
            nombre_archivo="datos.txt"
        if datos is None:
            datos = "No hay datos"
        ruta_txt = "{}/txt/{}".format(self.ruta_static,nombre_archivo)
        with open(ruta_txt, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
            f.write(str(datos))
        return True # booleano True (1) False (0)

    #def graficar_rectas(self,recta_empinada, recta_plana, recta_abajo):
    def graficar_rectas(self,a, n,x):
        # recta_empinada 0.0, recta_plana 0.0, recta_abajo 0.0 0.0=float 0=int 6545646546 = double
        f = (a*x)**n
        print("funcion_calculo:",f)

    ruta_archivo=""
    
# Llamamos a la función para escribir el archivo JSON

# vamos crea una intancia de la clase
ingestion = Actividad_1()

datos_json = ingestion.leer_api("https://jsonplaceholder.typicode.com/photos")
ruta="src/static/json/js.json"
#datos_json = ingestion.leer_json("https://jsonplaceholder.typicode.com/photos")
print("datos json:",datos_json)
if ingestion.escribir_json(ruta,datos_json):
    print("se creo el archivo se guardo el json")
    
datos_json = ingestion.leer_api("https://api.github.com/users/octocat")
"https://api.nbp.pl/api/exchangerates/tables/{table}/"
datos_json = ingestion.leer_api("https://api.nbp.pl/api/exchangerates/tables/B/")

datos_json = ingestion.leer_api("https://www.amiiboapi.com/api/amiibo/?character=zelda&showusage")
print("datos json:",datos_json)
if ingestion.escribir_txt(nombre_archivo="entrega_actividad_1.txt",datos=datos_json):
    print("se creo el archivo txt")
print("esta es la ruta statica :",ingestion.ruta_static)

for n in  range(0,10):
    ingestion.graficar_rectas(5, n, 5.4) 
    
# Llamamos a la función para escribir el archivo JSON.escribir_json(ruta_archivo, datos)
    
    