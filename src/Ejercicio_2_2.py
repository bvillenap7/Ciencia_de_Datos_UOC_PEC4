# This software is MIT licensed (see LICENSE)

from Ejercicio_1_2 import csv_to_dataframe
import os
import pandas as pd


def crear_diccionario(ruta=None):
    """
    Esta función crea un diccionario ordenado
    cuya clave será el nombre de la serie (name) y
    cuyo valor será la dirección web completa de su
    poster (homepage y poster_path).

    En caso de que homepage o poster_path tengan el valor
    NaN o "", el valor será el string “NOT AVAILABLE”.

    A su vez, esta función muestra por pantalla los primeros
    5 registros del diccionario.

    """

    if ruta is None:
        ruta_1 = os.path.join(os.getcwd(), 'data')
        t1, dataframe = csv_to_dataframe(ruta_1)
    else:
        t1, dataframe = csv_to_dataframe(ruta)

    diccionario = {}

    for index, row in dataframe.iterrows():

        name = row['name']
        web = row['homepage']
        p_path = row['poster_path']

        if pd.isna(web) or web == '':
            web = 'NOT AVAILABLE'
        else:
            pass

        if pd.isna(p_path) or p_path == '':
            p_path = 'NOT AVAILABLE'
        else:
            pass

        diccionario[name] = (web, p_path)

    dicc = {k: v for k, v in diccionario.items()}

    print("Los 5 primeros registros del diccionario son:\n\n")

    for k, v in list(dicc.items())[:5]:
        print(f"{k}: {v}")

    return dicc
