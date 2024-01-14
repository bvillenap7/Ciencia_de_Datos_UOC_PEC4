# This software is MIT licensed (see LICENSE)
import pandas as pd
import os
import time


def csv_to_dataframe(ruta_archivos):
    """
    Esta función recoge como parámetro la ruta
    dónde se encuentran los archivos csv y los
    integra dentro de un DataFrame utilizando
    como clave la columna "id" y utilizando la
    librería pandas.

    A su vez, la propia función nos devuelve
    el tiempo de procesamiento al ejecutarla.

    PAra ello usa la librería pandas
    """
    # Iniciamos cronómetro
    inicio = time.time()

    # Integramos los archivos csv de la ruta
    # especificada, en un solo DataFrame

    archivo_csv = []
    dataframe_csv = []

    for archivo in os.listdir(ruta_archivos):
        if archivo.endswith('.csv'):
            archivo_csv.append(archivo)

    for csv in archivo_csv:
        ruta_csv = os.path.join(ruta_archivos, csv)
        df = pd.read_csv(ruta_csv)
        dataframe_csv.append(df)

    df_completo = pd.merge(dataframe_csv[0], dataframe_csv[1], on='id', how='inner')
    df_completo = pd.merge(df_completo, dataframe_csv[2], on='id', how='inner')
    # Terminanos de calcular el tiempo de ejecución
    fin = time.time()

    tiempo_ejecucion = fin - inicio

    print(f'El tiempo de conversión de CSV a DataFrame con Pandas '
          f'es de {round(tiempo_ejecucion, 4)} segundos')

    return tiempo_ejecucion, df_completo

