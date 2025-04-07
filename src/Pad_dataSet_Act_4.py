import pandas as pd
import kagglehub
import os
import zipfile
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter
# tkinter._test()
import numpy as np


class Pad_dataSet:
    def __init__(self):
        pass
        
    def download_dataset_zip(self):
        print("Descargando dataset desde Kaggle...")
        dataset_path = kagglehub.dataset_download("jaforero/baloto-colombia")
        print("Ruta al dataset:", dataset_path)
        return dataset_path
    
    def extract_zip_files(self,dataset_path):
        zip_files = [f for f in os.listdir(dataset_path) if f.endswith('.zip')]
        if zip_files:
            zip_file = os.path.join(dataset_path, zip_files[0])
            extract_dir = os.path.join(dataset_path, "extracted")
            os.makedirs(extract_dir, exist_ok=True)
            print(f"Extrayendo {zip_file} en {extract_dir}...")
            with zipfile.ZipFile(zip_file, "r") as z:
                z.extractall(extract_dir)
            return extract_dir
        else:
            # Si no se encuentra un ZIP, se verifica si existen archivos CSV en la ruta
            csv_files = [f for f in os.listdir(dataset_path) if f.endswith('.csv')]
            if csv_files:
                print("No se encontró archivo ZIP pero se detectaron archivos CSV; se asume que el dataset ya se encuentra extraído.")
                return dataset_path
            else:
                raise FileNotFoundError("No se encontró ningún archivo .zip ni archivos .csv en la ruta del dataset")

    def create_csv(self,csv_dir):
        os.makedirs('src/static/csv', exist_ok=True)
        #db_path = 'src/static/db/ingestion.db'

        # # Eliminar el archivo de base de datos si ya existe
        # if os.path.exists(db_path):
        #     print(f"Eliminando base de datos existente en {db_path}...")
        #     os.remove(db_path)

        csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
        if not csv_files:
            raise FileNotFoundError("No se encontraron archivos CSV en el directorio extraído")

        for file in csv_files:
            file_path = os.path.join(csv_dir, file)
            print(f"Leyendo {file_path}...")
            try:
                df = pd.read_csv(file_path, encoding="latin1")
            except Exception as e:
                print(f"Error al leer {file}: {e}")
                continue
            print(f"Creando/actualizando ")
        print("cvs creado correctamente en ")
        return df

        
        
        


# padclase = Pad_dataSet()          
# dataset_path = padclase.download_dataset_zip()
# csv_dir = padclase.extract_zip_files(dataset_path)
# df = padclase.create_csv(csv_dir)
# print(df.head())
# print(df.describe(),df.count,df.info())
# df.to_csv("dataset_kaggle.csv")
# padclase.grafico_normal(df)
# padclase.grafico_df_xy(df)
# #209306
# #print(df.describe(),df.count,df.info())