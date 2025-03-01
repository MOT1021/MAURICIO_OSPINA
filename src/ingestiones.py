import json
import requests

# Inicializando el diccionario para contabilizar las tareas completadas por usuario
tareas_completadas_por_usuario = {}



url = "https://jsonplaceholder.typicode.com/todos"
respuesta_api = requests.get(url)

# Convertir la respuesta en formato JSON a una estructura de datos de Python
lista_tareas = json.loads(respuesta_api.text)

print(lista_tareas) 

# Recorrer la lista de tareas
for tarea in lista_tareas:
    if tarea["completed"]:
        usuario_id = tarea["userId"]
        try:
            # Intentar incrementar el contador para el usuario existente
            tareas_completadas_por_usuario[usuario_id] += 1
        except KeyError:
            # Si el usuario no está en el diccionario, agregarlo con un contador de 1
            tareas_completadas_por_usuario[usuario_id] = 1

usuarios_ordenados = sorted(tareas_completadas_por_usuario.items(), key=lambda x: x[1], reverse=True)
# Determinar el máximo número de tareas completadas
max_completadas = usuarios_ordenados[0][1]
usuarios_max = []

for usuario, num_completadas in usuarios_ordenados:
    if num_completadas < max_completadas:
        break
    usuarios_max.append(str(usuario))

# Crear una cadena con los usuarios que más tareas completaron
usuarios_max_str = " y ".join(usuarios_max)

print(f"Usuario(s) {usuarios_max_str} completaron {max_completadas} tareas")



class Ingestiones():    
    def __init__(self):
        self.ruta_static="src/static/"
    def leer_json(self):
        # r read w write

        ruta_json = "{}json/datos_persona.json".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = json.load(f)
        return datos    


    def leer_txt(self):
        # r read w write

        ruta_json = "{}txt/info.txt".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos 
    
  



    def leer_varios_txt(self,nombre=""):
        # r read w write

        ruta_txt = "{}txt/{}".format(self.ruta_static,nombre)
        datos=""
        with open(ruta_txt,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos   
    
    def  leer_cualquier_excel(self,nombre=""):
        pass
    
    def  leer_cualquier_csv(self,nombre=""):
        pass
    
    def  leer_html(self,url=""):
        pass
    
    def  leer_bd(self,nombre_bd="",servidor="",puerto=0000):
        pass
    
    def  leer_api(self,url="https://jsonplaceholder.typicode.com/todos"):
        pass
    
    def escribir_txt(self,nombre,datos):
        # r read w write

        ruta_txt = "{}.txt".format(nombre)
        datos=""
        with open(ruta_txt,"w",encoding="utf-8") as f:
            #f.write(datos)
            f.writelines(datos)

inges = Ingestiones() 
datos_json = inges.leer_json()
print(datos_json)
print("************************************************************")
print("************************************************************")
datos_txt = inges.leer_txt()
print(datos_txt)
print("************************************************************")
print("************************************************************")
nombre_archivo = "info copy.txt"
datos_txt_dos = inges.leer_varios_txt(nombre_archivo)
print(datos_txt_dos)
print("************************************************************")
print("************************************************************")
print("Primeros dos elementos de la lista de tareas:", lista_tareas[:2])
print("************************************************************")
print("************************************************************")
print(f"Usuario(s) {usuarios_max_str} completaron {max_completadas} tareas")


inges.escribir_txt(nombre="archivo_json",datos=datos_json)
inges.escribir_txt(nombre="archivo_txt",datos=datos_txt)
inges.escribir_txt(nombre="archivo_txt_copy",datos=datos_txt_dos)
    