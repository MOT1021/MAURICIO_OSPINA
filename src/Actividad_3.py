import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from Pad_dataSet import Pad_dataSet
from data_set_act_3 import ACT_3_dataSet

class actividad3:
    def __init__(self):
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/actividad_3/".format(self.ruta_raiz)
        datos = {
            "Numero_punto": [1,2,3,4,5,6,7,8,9,10,11,12],
            "Detalle":["","","","","","","","","","","",""],
            "Resultado":[0,0,0,0,0,0,0,0,0,0,0,0],
            
        }
        self.df = pd.DataFrame(datos)
        print(self.ruta_raiz)
        
    def punto_1(self):
        frutas = pd.DataFrame({
            'Granadilla': [20],
            'Tomates': [50]
        })

        # Mostrar el DataFrame
        print(frutas)
        
        self.df.loc[0,"Resultado"] = frutas.to_csv(index=0)
        self.df.loc[0,"Detalle"] = "Crea un DataFrame frutas que luzca así"
        print("punto_1")
             
    def punto_2(self):
        ventas_frutas = pd.DataFrame(
            {
                "Granadilla": [20, 49],
                "Tomates": [50, 100],
            },
            index=["ventas 2021", "ventas 2022"]  # Definir los nombres de las filas
        )

        # Mostrar el resultado
        print(ventas_frutas)
        self.df.loc[1,"Detalle"] =  " Crea un DataFrame ventas_frutas que coincida con el diagrama"    
        self.df.loc[1,"Resultado"] = ventas_frutas.to_csv(index=1)  
        print("punto_2") 
        
    def punto_3(self):
        utensilios = pd.Series(
        ["3 unidades", "2 unidades", "4 unidades", "5 unidades"],
        index=["Cuchara", "Tenedor", "Cuchillo", "Plato"],
        name="Cocina")
        
        print(utensilios)
        self.df.loc[2,"Resultado"] = utensilios.to_csv(index=2)
        self.df.loc[2,"Detalle"] =  "Crea una variable utensilios con una Serie que tenga el siguiente aspecto" 
        print("punto_3")
         
    def punto_4(self):
        padclase = ACT_3_dataSet()
        dataset_path = padclase.download_dataset_zip()
        csv_dir = padclase.extract_zip_files(dataset_path)
        df = padclase.create_csv(csv_dir)
        # print(df.describe(),df.count,df.info())
        print(df)
        self.df.loc[3,"Resultado"] = "se ejecuto el punto 4 de la actividad 3"
        self.df.loc[3,"Detalle"] =  "Descarga el dataset 'wine review' desde Kaggle y cárgalo en un DataFrame llamado review, tal y como se muestra en la figura."
        print("punto_4") 
        
    def punto_5(self):
        padclase = ACT_3_dataSet()
        dataset_path = padclase.download_dataset_zip()
        csv_dir = padclase.extract_zip_files(dataset_path)
        df = padclase.create_csv(csv_dir)
        # print(df.describe(),df.count,df.info())
        print(df.head(10))
        self.df.loc[4,"Resultado"] = "se ejecuto el punto 5 de la actividad 3"
        self.df.loc[4,"Detalle"] =  "Visualiza las primeras filas del DataFrame"
        print("punto_5") 
        
    def punto_6(self):
        padclase = ACT_3_dataSet()
        dataset_path = padclase.download_dataset_zip()
        csv_dir = padclase.extract_zip_files(dataset_path)
        df = padclase.create_csv(csv_dir)
        print(df.info())
        self.df.loc[5,"Resultado"] = "se ejecuto el punto 6 de la actividad 3"
        self.df.loc[5,"Detalle"] =  "Utiliza el método .info() para averiguar cuántas entradas hay. ¿Cuántas encontraste?"
        print("punto_6") 
        
    def punto_7(self):
        padclase = ACT_3_dataSet()
        dataset_path = padclase.download_dataset_zip()
        csv_dir = padclase.extract_zip_files(dataset_path)
        df = padclase.create_csv(csv_dir)
        precio_promedio = df["price"].mean() 
        self.df.loc[6,"Resultado"] = f"El precio promedio es: $ {precio_promedio:.2f}"
        self.df.loc[6,"Detalle"] =  "¿Cuál es el precio promedio?"
        print(f"El precio promedio es: ${precio_promedio:.2f}")
        print("punto_7") 
        
    def punto_8(self):
        padclase = ACT_3_dataSet()
        dataset_path = padclase.download_dataset_zip()
        csv_dir = padclase.extract_zip_files(dataset_path)
        df = padclase.create_csv(csv_dir)
        precio_max = df["price"].max() 
        self.df.loc[7,"Resultado"] = f"El precio más alto pagado es: {precio_max}"
        self.df.loc[7,"Detalle"] =  "¿Cuál es el precio más alto pagado?"
        print(f"El precio más alto pagado es: ${precio_max}")
        print("punto_8") 
        
    def punto_9(self):
        padclase = ACT_3_dataSet()
        dataset_path = padclase.download_dataset_zip()
        csv_dir = padclase.extract_zip_files(dataset_path)
        df = padclase.create_csv(csv_dir)
        vinos_california = df[df["province"] == "California"]
        self.df.loc[8,"Resultado"] = "Se ejecuto punto 9 de la actividad 3"
        self.df.loc[8,"Detalle"] =  "Crea un DataFrame con todos los vinos de california. Salida esperada:"

        # Mostrar las primeras filas del nuevo DataFrame
        print(vinos_california)
        print("punto_9") 
        
    def punto_10(self):
        padclase = ACT_3_dataSet()
        dataset_path = padclase.download_dataset_zip()
        csv_dir = padclase.extract_zip_files(dataset_path)
        df = padclase.create_csv(csv_dir)
        
        indice_max_precio = df["price"].idxmax()

        vino_mas_caro = df.loc[indice_max_precio]

        print(vino_mas_caro)
        
        self.df.loc[9,"Resultado"] = "Se ejecuto punto 10 de la actividad 3"
        self.df.loc[9,"Detalle"] =  "Utiliza idxmax() para encontrar el índice del vino con el precio más alto y luego utiliza loc para obtener toda la información de ese vino específico."
        print("punto_10") 
        
    def punto_11(self):
        padclase = ACT_3_dataSet()
        dataset_path = padclase.download_dataset_zip()
        csv_dir = padclase.extract_zip_files(dataset_path)
        df = padclase.create_csv(csv_dir)        
        vinos_california = df[df["province"] == "California"]
        variedades_comunes = vinos_california["variety"].value_counts()
        print(variedades_comunes)
        self.df.loc[10,"Resultado"] = "Se ejecuto punto 11 de la actividad 3"
        self.df.loc[10,"Detalle"] =  " Cuáles son los tipos de uva más comunes en California? "
        print("punto_11") 
        
    def punto_12(self,num=100):
        padclase = ACT_3_dataSet()
        dataset_path = padclase.download_dataset_zip()
        csv_dir = padclase.extract_zip_files(dataset_path)
        df = padclase.create_csv(csv_dir)        
        vinos_california = df[df["province"] == "California"]
        variedades_comunes = vinos_california["variety"].value_counts()
        print(variedades_comunes.head(10))
        self.df.loc[11,"Resultado"] = "Se ejecuto punto 12 de la actividad 3"
        self.df.loc[11,"Detalle"] =  " ¿Cuáles son los 10 tipos de uva más comunes en California?"
        print("punto_11") 
        
    
    def ejecutar(self):
        self.punto_1()     
        self.punto_2() 
        self.punto_3() 
        self.punto_4() 
        self.punto_5() 
        self.punto_6() 
        self.punto_7() 
        self.punto_8() 
        self.punto_9() 
        self.punto_10()
        self.punto_11()
        self.punto_12()
        self.df.to_csv("actividad3.csv")
        
act = actividad3()
act.ejecutar()