# This software is MIT licensed (see LICENSE)

from Ejercicio_1_2 import csv_to_dataframe
import os
import pandas as pd


def add_days(ruta=None):
    """
    Esta función agrega una nueva columna al dataframe
    creado por la función csv_to_dataframe. Esta nueva
    columna contiene el número de días que estuvo en
    emisión la serie en cuestión.

    """

    if ruta is None:
        ruta_1 = os.path.join(os.getcwd(), 'data')
        t1, dataframe = csv_to_dataframe(ruta_1)
    else:
        t1, dataframe = csv_to_dataframe(ruta)

    dataframe['first_air_date'] = pd.to_datetime(dataframe
                                                 ['first_air_date'])
    dataframe['last_air_date'] = pd.to_datetime(dataframe
                                                ['last_air_date'])

    dataframe['air_days'] = (dataframe['last_air_date'] -
                            (dataframe['first_air_date']))

    df = dataframe.sort_values(by='air_days', ascending=False)

    top_10 = df.head(10)
    print(top_10)

    return dataframe
