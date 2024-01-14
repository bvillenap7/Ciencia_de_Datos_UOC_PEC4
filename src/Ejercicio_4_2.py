# This software is MIT licensed (see LICENSE)

import matplotlib.pyplot as plt
import pandas as pd
import os
from Ejercicio_1_2 import csv_to_dataframe


def grafico_by_decade(ruta=None):

    """
    Esta función, partiendo de los archivos CSV,
    muestra en un gráfico de de líneas que muestra
    el número de series de cada categoría de la variable
    “type” producidas en cada década desde 1940

    :param ruta: Ruta dónde se encuentran los archivos
    CSV que queremos analizar

    :return: Devuelve un gráfico de líneas.
    """

    if ruta is None:
        ruta_1 = os.path.join(os.getcwd(), 'data')
        t1, dataframe = csv_to_dataframe(ruta_1)
    else:
        t1, dataframe = csv_to_dataframe(ruta)

    dataframe['first_air_date'] = pd.to_datetime(dataframe['first_air_date'])
    dataframe = dataframe.dropna(subset=['first_air_date'])
    dataframe = dataframe[dataframe['first_air_date'].dt.year >= 1940]
    dataframe['decada'] = (dataframe['first_air_date'].dt.year // 10) * 10
    decada = dataframe.groupby(['decada', 'type']).size().unstack()

    fig, ax = plt.subplots(figsize=(30, 6))
    decada.plot(kind='line', marker='s', ax=ax, alpha=0.4)
    ax.set_title('Número de Series por Año de Inicio')
    ax.set_xlabel('Año de Inicio')
    ax.set_ylabel('Número de Series')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()

    return fig
