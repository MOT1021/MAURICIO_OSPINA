import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class actividad2:
    def __init__(self):
        self.df=pd.DataFrame(columns=["# Ejercicio","valor"])
        
    def punto_1(self):
        array_10_20 = np.arange(10,20)
        self.df["# Ejercicio"]=1
        self.df["valor"]=array_10_20
        self.df.to_excel("Actividad_2.xlsx")
 
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/".format(self.ruta_raiz)
        print(self.ruta_raiz)
        #print(data)
    def punto_11(self,num=100):
        x = np.random.rand(num)
        y = np.random.rand(num)
        plt.scatter(x,y)
        ruta = "{}punto_11.png".format(self.ruta_act2)
        plt.savefig(ruta)
        print(f"Imagen guardada en: {ruta}")
        
act = actividad2()
act.punto_11()
act.punto_1()

