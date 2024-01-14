# This software is MIT licensed (see LICENSE)

from Ejercicio_1_2 import csv_to_dataframe
import os

def show(ruta=None):

    """
    Esta función obtiene y muestra por pantalla los nombres
    de las series cuyo idioma original (original_language)
    sea el inglés y en cuyo resumen (overview) aparezcan
    las palabras “mystery” o “crime”, sin tener en cuenta
    mayúsculas ni minúsculas.
    """

    if ruta is None:
        ruta_1 = os.path.join(os.getcwd(), 'data')
        t1, dataframe = csv_to_dataframe(ruta_1)
    else:
        t1, dataframe = csv_to_dataframe(ruta)

    filtro = dataframe[
        (dataframe['original_language'] == 'en') &
        (dataframe['overview'].str.contains('mystery|crime'))
        ]

    nombres = filtro['name'].tolist()

    print('Las series cuyo idioma original es el inglés'
          ' y en cuyo resumen (overview) aparecen las palabras'
          f' mystery o crime son:')
    for nombre in nombres:
        print(nombre)

    return nombres