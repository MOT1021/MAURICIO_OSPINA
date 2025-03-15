import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class actividad2:
    def __init__(self):
        self.df = pd.DataFrame(columns=["# Ejercicio", "valor"])
        self.ruta_raiz = os.path.abspath(os.getcwd())  # Ruta base del proyecto
        self.ruta_ejercicios = os.path.join(self.ruta_raiz, "src","Ejercicios")  # Carpeta de salida

        # Crear la carpeta "Ejercicios" si no existe
        if not os.path.exists(self.ruta_ejercicios):
            os.makedirs(self.ruta_ejercicios)

    def punto_1(self):
        array_10_29 = np.arange(10, 29)

        for i, val in enumerate(array_10_29):
            self.df.loc[i] = [1, val]

        # Guardar archivo Excel 
        ruta_excel = os.path.join(self.ruta_ejercicios, "Actividad_2.xlsx")
        self.df.to_excel(ruta_excel, index=False)
        print(f"Excel guardado en: {ruta_excel}")
        
    def punto_2(self):
        array_10x10 = np.ones((10, 10))
        suma_total = np.sum(array_10x10)
        print(suma_total)
     

    def punto_11(self, num=100):
        x = np.random.rand(num)
        y = np.random.rand(num)
        plt.scatter(x, y)

        # Guardar imagen 
        ruta_imagen = os.path.join(self.ruta_ejercicios, "punto_11.png")
        plt.savefig(ruta_imagen)
        print(f"Imagen guardada en: {ruta_imagen}")

# instancia de la clase y ejecuta
act = actividad2()
#act.punto_11()
act.punto_2()
