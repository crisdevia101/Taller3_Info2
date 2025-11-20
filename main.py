import os
import pydicom
import pandas as pd
import numpy as np

class ProcesadorDICOM:
    def __init__(self, ruta):
        self.ruta = ruta
        self.archivos_dicom = []
        self.dataframe = None

    def cargar_archivos(self):
        for archivo in os.listdir(self.ruta):
            ruta_comp = os.path.join(self.ruta, archivo)
            try:
                dicom = pydicom.dcmread(ruta_comp)
                self.archivos_dicom.append(dicom)
            except Exception:
                print("{arhivo} no es un archivo DICOM valido")

    def extraer_metadatos(self):
        datos = []

        for dicom in self.archivos_dicom:
            info = {
                "PacienteID": getattr(dicom, "PatientID", "No disponible"),
                "NombrePaciente": getattr(dicom, "PatientName", "No disponible"),
                "StudyInstanceUID": getattr(dicom, "StudyInstanceUID", "No disponible"),
                "StudyDescription": getattr(dicom, "StudyDescription", "No disponible"),
                "StudyDate": getattr(dicom, "StudyDate", "No disponible"),
                "Modality": getattr(dicom, "Modality", "No disponible"),
                "Rows": getattr(dicom, "Rows", "No disponible"),
                "Columns": getattr(dicom, "Columns", "No disponible"),
            }
            datos.append(info)

        self.dataframe = pd.DataFrame(datos)

    def calcular_intensidad_promedio(self):
        intensidades = []

        for dicom in self.archivos_dicom:
            try:
                promedio = np.mean(dicom.pixel_array)
            except Exception:
                promedio = None
            intensidades.append(promedio)

        self.dataframe["IntensidadPromedio"] = intensidades
    
    def obtener_dataframe(self):
        return self.dataframe

if __name__ == "__main__":
    #ruta = "Sarcoma\img1" #Si se hace solo con la misma ruta
    ruta = input("Ruta de los archivos: )
                 #Para ingresar cualquier ruta con archivos dcm

    procesador = ProcesadorDICOM(ruta)
    procesador.cargar_archivos()
    procesador.extraer_metadatos()
    procesador.calcular_intensidad_promedio()

    df = procesador.obtener_dataframe()
    print(df)

    df.to_csv("metadatos_dicom.csv", index=False)
    print("Archivo generado correctamente")
