# This software is MIT licensed (see LICENSE)

from Ejercicio_1_2 import csv_to_dataframe
import os

def cancel(ruta=None):

    """
    Esta función obtiene una lista de las series
    que han empezado en 2023 y han sido canceladas.
    A su vez, muestra por pantalla los primeros 20
    elementos de esta lista.
    """

    if ruta is None:
        ruta_1 = os.path.join(os.getcwd(), 'data')
        t1, dataframe = csv_to_dataframe(ruta_1)
    else:
        t1, dataframe = csv_to_dataframe(ruta)

    dataframe['first_air_date'] = dataframe['first_air_date'].astype(str)
    filtro = dataframe[
        (dataframe['status'] == 'Canceled') &
        (dataframe['first_air_date'].str.contains('2023'))
        ]

    nombres = filtro['name'].tolist()

    print('Las 20 primeras peliculas de la lista '
          'de peliculas canceladas y empezadas en 2023'
          ' son:\n' + '\n'.join(n for n in nombres[:20]))

    return nombres