# This software is MIT licensed (see LICENSE)

import matplotlib.pyplot as plt
import pandas as pd
import os
from Ejercicio_1_2 import csv_to_dataframe


def grafico_by_year(ruta=None):

    """
    Esta función, partiendo de los archivos CSV,
    muestra en un gráfico de barras el
    número de series por año de inicio.

    :param ruta: Ruta dónde se encuentran los archivos
    CSV que queremos analizar

    :return: Devuelve un gráfico de barras.
    """

    if ruta is None:
        ruta_1 = os.path.join(os.getcwd(), 'data')
        t1, dataframe = csv_to_dataframe(ruta_1)
    else:
        t1, dataframe = csv_to_dataframe(ruta)

    dataframe['first_air_date'] = pd.to_datetime(dataframe['first_air_date'])
    dataframe = dataframe.dropna(subset=['first_air_date'])
    year = dataframe.groupby(dataframe['first_air_date'].dt.year)['name'].count()
    year = year[year > 0]

    fig, ax = plt.subplots(figsize=(30, 6))
    bars = ax.bar(year.index, round(year, 0), color='green', alpha=0.7,)

    ax.set_xticks(year.index)
    ax.set_xticklabels(year.index, rotation=75, size=6)
    y_ticks = ax.get_yticks()
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_ticks, rotation=15, size=8)
    ax.set_title('Número de Series por Año de Inicio')
    ax.set_xlabel('Año de Inicio')
    ax.set_ylabel('Número de Series')
    for bar in bars:
        y = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, y + 0.1, round(y, 0),
                ha='center', va='bottom', rotation=75, size=5)
    plt.show()
    return fig
