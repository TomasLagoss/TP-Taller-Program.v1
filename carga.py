import csv
import os

def cargar_telemetria(ruta_archivo): 
    if not os.path.exists(ruta_archivo):
        raise FileExistsError("No se encontro el archivo: " + ruta_archivo)
    datos = [] #Crea una lista vacía para almacenar los datos
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fila["ping_promedio"] = int(fila['ping_promedio'])
            fila["fps_promedio"] = int(fila['fps_promedio'])
            fila["id_sesion"] = int(fila["id_sesion"])
            fila["duracion_minutos"] = float(fila["duracion_minutos"])
            fila["intentos_fallidos"] = int(fila["intentos_fallidos"])
            fila["reportes_trampa"] = int(fila["reportes_trampa"])
            datos.append(fila)

    if len(datos) == 0:
        raise ValueError("El archivo no contiene sesiones.")

    return datos
