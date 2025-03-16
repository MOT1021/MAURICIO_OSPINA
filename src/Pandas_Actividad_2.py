import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class actividad2:
    def __init__(self):
        Datos=[(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0)]
        #Datos=[(1,0),(2,0),(3,0),(4,0)(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0)]
        self.df=pd.DataFrame(data=Datos,columns=["# Ejercicio","valor"])
        
        
    def punto_1(self):
        array_10_20 = np.arange(10,20)
        #self.df["# Ejercicio"]=1
        #self.df["valor"]=str(array_10_20)
        self.df.iloc[0,1]= str(array_10_20)
        self.df.to_excel("src/Ejercicios/Actividad_2.xlsx",index= False )
        print("se ejecutó - PUNTO 1")
 
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/Ejercicios/".format(self.ruta_raiz)
        print(self.ruta_raiz)
        #print(data)
        
    def punto_2(self):
        array_10x10 = np.ones((10, 10))
        suma_total = np.sum(array_10x10)
        self.df.iloc[1,1]= suma_total
        print(suma_total)
        self.df.to_excel("src/Ejercicios/Actividad_2.xlsx",index= False )
        print("se ejecutó - PUNTO 2")
        
    def punto_3(self):
        # Crear dos arrays de tamaño 5 con números aleatorios entre 1 y 10
        array1 = np.random.randint(1, 11, size=5)
        array2 = np.random.randint(1, 11, size=5)

        # Realizar el producto elemento a elemento
        producto_elemento_a_elemento = array1 * array2
        print("Array 1:", array1)
        print("Array 2:", array2)
        print("Producto elemento a elemento:", producto_elemento_a_elemento)
        self.df.iloc[2,1]= str(producto_elemento_a_elemento)
        self.df.to_excel("src/Ejercicios/Actividad_2.xlsx",index= False )
        print("se ejecutó - PUNTO 3")
    
    def punto_4(self):
        np.random.seed(0)  # Fijar semilla para reproducibilidad
        matriz = np.array([[i + j + np.random.rand() for j in range(4)] for i in range(4)])
        inversa = np.linalg.inv(matriz)
        self.df.iloc[3,1]= str(inversa)
        self.df.to_excel("src/Ejercicios/Actividad_2.xlsx",index= False )
        print("Matriz ",matriz)
        print("Matriz Inversa ",inversa)
        print("se ejecutó - PUNTO 4")
    
    def punto_5(self):
        # Crear un array de 100 elementos aleatorios
        array_random = np.random.rand(100)

        maximo = np.max(array_random)
        indice_maximo = np.argmax(array_random)
        
        minimo = np.min(array_random)
        indice_minimo = np.argmin(array_random)
        print("Array de 100 elementos aleatorios:", array_random)
        print("Valor máximo:", maximo, "en el índice:", indice_maximo)
        print("Valor mínimo:", minimo, "en el índice:", indice_minimo)
        con = np.vstack((maximo,minimo,indice_maximo,indice_minimo))
        self.df.iloc[4,1]= str(con)
        self.df.to_excel("src/Ejercicios/Actividad_2.xlsx",index= False )
        print("se ejecutó - PUNTO 5")
    
    def punto_6(self):
        # Crear un array de tamaño 3x1
        array_3x1 = np.array([[1], [2], [3]])
        array_1x3 = np.array([[10, 20, 30]])
        resultado_broadcasting = array_3x1 + array_1x3
        #print(resultado_broadcasting)
        self.df.iloc[5,1]= str(resultado_broadcasting)
        self.df.to_excel("src/Ejercicios/Actividad_2.xlsx",index= False )
        print("se ejecutó - PUNTO 6")
    
    def punto_7(self):
        matriz_5x5 = np.arange(25).reshape(5, 5)
        submatriz = matriz_5x5[1:3, 1:3]
        print(matriz_5x5)
        print("Submatriz 2x2:", submatriz)
        self.df.iloc[6,1]= str(submatriz)
        self.df.to_excel("src/Ejercicios/Actividad_2.xlsx",index= False )
        print("se ejecutó - PUNTO 7")
    
    def punto_8(self):
        # Crear un array de ceros de tamaño 10
        array_zeros = np.zeros(10)

        array_zeros[3:7] = 5
        print("Array modificado:", array_zeros)
        self.df.iloc[7,1]= str(array_zeros)
        self.df.to_excel("src/Ejercicios/Actividad_2.xlsx",index= False )
        print("se ejecutó - PUNTO 8")
    
    def punto_9(self):
        # Crear una matriz 3x3
        matriz_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matriz_invertida = matriz_3x3[::-1, :]
        print("Matriz con filas invertidas:\n", matriz_invertida)
        self.df.iloc[8,1]= str(matriz_invertida)
        self.df.to_excel("src/Ejercicios/Actividad_2.xlsx",index= False )
        print("se ejecutó - PUNTO 9")
    
    def punto_10(self):
        # Crear un array de números aleatorios de tamaño 10
        array_random = np.random.rand(10)
        mayores_05 = array_random[array_random > 0.5]
        # print( array_random)
        print("Elementos mayores a 0.5:", mayores_05)
        self.df.iloc[9,1]= str(mayores_05)
        self.df.to_excel("src/Ejercicios/Actividad_2.xlsx",index= False )
        print("se ejecutó - PUNTO 10")
        
    def punto_11(self,num=100):
        x = np.random.rand(num)
        y = np.random.rand(num)
        plt.scatter(x,y)
        ruta = "{}punto_11.png".format(self.ruta_act2)
        plt.savefig(ruta)
        print(f"Imagen guardada en: {ruta}")
        
    def punto_12(self):
        # 1. Generar el array x en el rango de -2π a 2π
        x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
        ruido = np.random.normal(0, 0.2, size=x.shape)  # Ruido Gaussiano con media 0 y desviación estándar 0.2
        y_con_ruido = np.sin(x) + ruido
        y_sin_ruido = np.sin(x)
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y_con_ruido, color='blue', label='$y = \sin(x) + \text{ruido}$', alpha=0.6)
        plt.plot(x, y_sin_ruido, color='red', label='$y = \sin(x)$', linewidth=2)

        # Personalizar el gráfico
        plt.title('Gráfico de dispersión de $y = \sin(x) + \text{ruido}$ y $y = \sin(x)$')
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Línea horizontal en y=0
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Línea vertical en x=0
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        # plt.show()
        ruta = "{}punto_12.png".format(self.ruta_act2)
        plt.savefig(ruta)
        print(f"Imagen guardada en: {ruta}")

    def punto_13(self):
        pass
    
    def punto_14(self):
        pass
    
    def punto_15(self):
        pass
    
    def punto_16(self):
        pass
    
    def punto_17(self):
        pass
    
    def punto_18(self):
        pass
    
    def punto_19(self):
        pass
    
    def punto_20(self):
        pass
    
        
act = actividad2()
act.punto_1()
# act.punto_2()
# act.punto_3()
# act.punto_4()
# act.punto_5()
# act.punto_6()
# act.punto_7()
# act.punto_8()
# act.punto_9()
# act.punto_10()
# act.punto_11()
act.punto_12()
# act.punto_13()
# act.punto_14()
# act.punto_15()
# act.punto_16()
# act.punto_17()
# act.punto_18()
# act.punto_19()
# act.punto_20()


