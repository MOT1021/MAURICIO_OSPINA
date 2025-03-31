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
        print(df.head())
        self.df.loc[3,"Resultado"] = "se ejecuto el punto 4 de la actividad 3"
        self.df.loc[2,"Detalle"] =  "Descarga el dataset 'wine review' desde Kaggle y cárgalo en un DataFrame llamado review, tal y como se muestra en la figura."
        print("punto_4") 
        
    def punto_5(self):
        self.df.loc[4,"Resultado"] = len(self.df)+4
        print("punto_5") 
        
    def punto_6(self):
        self.df.loc[5,"Resultado"] = "punto_5.csv"
        print("punto_6") 
        
    def punto_7(self):
        self.df.loc[6,"Resultado"] = len(self.df)+6
        print("punto_7") 
        
    def punto_8(self):
        self.df.loc[7,"Resultado"] = len(self.df)+7
        print("punto_8") 
        
    def punto_9(self):
        self.df.loc[8,"Resultado"] = len(self.df)+8
        print("punto_9") 
        
    def punto_10(self):
        self.df.loc[9,"Resultado"] = len(self.df)+9
        print("punto_10") 
        
    def punto_11(self):
        self.df.loc[10,"Resultado"] = len(self.df)+10
        print("punto_11") 
        
    def punto_12(self,num=100):
        self.df.loc[11,"Resultado"] = len(self.df)+11
        print("punto_12") 
        
    
    def ejecutar(self):
        # self.punto_1()     
        # self.punto_2() 
        # self.punto_3() 
        self.punto_4() 
        # self.punto_5() 
        # self.punto_6() 
        # self.punto_7() 
        # self.punto_8() 
        # self.punto_9() 
        # self.punto_10()
        # self.punto_11()
        # self.punto_12()
        self.df.to_csv("actividad3.csv")
        
act = actividad3()
act.ejecutar()