# This software is MIT licensed (see LICENSE)
import csv
import os
import time
import pandas as pd


def csv_to_df_bycsv(ruta_archivos):
    """
    Esta función recoge como parámetro la ruta
    dónde se encuentran los archivos csv y los
    integra dentro de un DataFrame utilizando
    como clave la columna "id" y utilizando la
    librería pandas.

    A su vez, la propia función nos devuelve
    el tiempo de procesamiento al ejecutarla.

    Para ello usa la librería csv
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

    for c in archivo_csv:
        ruta_csv = os.path.join(ruta_archivos, c)
        with open(ruta_csv, 'r', encoding='utf-8',
                  newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            dataframe_csv.append(pd.DataFrame(list(csv_reader)))

    df_completo = dataframe_csv[0]

    for i in range(1, len(dataframe_csv)):
        df_completo = pd.merge(df_completo, dataframe_csv[i],
                               on='id')

    fin = time.time()

    tiempo_ejecucion = fin - inicio

    print(f'El tiempo de conversión de CSV a DataFrame con CSV library '
          f'es de {round(tiempo_ejecucion, 4)} segundos')

    return tiempo_ejecucion, df_completo
