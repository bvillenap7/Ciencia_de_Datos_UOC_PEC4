# This software is MIT licensed (see LICENSE)

import matplotlib.pyplot as plt
import os
from Ejercicio_1_2 import csv_to_dataframe


def grafico_circular(ruta=None):

    """
    Esta función, obtiene el número de series
    por género y muestra el porcentaje respecto
    al total en un gráfico circular.

    Los géneros que representen menos del 1% del
    total se incluirán en la categoría "Other".

    Tened en cuenta que una serie que tenga más
    de un género se incluirá en todas las
    categorías en que esté clasificada y que las
    series con el campo "genres" vacío no se
    incluyen.

    :param ruta: Ruta dónde se encuentran los archivos
    CSV que queremos analizar

    :return: Devuelve un gráfico circular.
    """

    if ruta is None:
        ruta_1 = os.path.join(os.getcwd(), 'data')
        t1, dataframe = csv_to_dataframe(ruta_1)
    else:
        t1, dataframe = csv_to_dataframe(ruta)

    dataframe = dataframe.dropna(subset=['genres'])
    genero = dataframe['genres'].str.split(',').explode().str.strip()
    frecuencia = genero.value_counts()
    total = len(dataframe)
    porcentaje = (frecuencia / total) * 100
    filtro = porcentaje[porcentaje >= 1]
    other = porcentaje[porcentaje < 1].sum()
    filtro['Other'] = other

    fig, ax = plt.subplots(figsize=(10, 10))

    wedges, texto = ax.pie(filtro, labels=(filtro.index),
                           startangle=90, rotatelabels=True,
                           textprops={'fontsize': 8}, pctdistance=0.9,
                           labeldistance=1.1)

    labels = ['{} - {}'.format(label,
                               '%1.1f%%' % pct) for label, pct in zip(filtro.index,
                                                                        filtro)]
    plt.legend(wedges, labels, title="Género",
               loc="center right", bbox_to_anchor=(1, 0, 0.5, 1),
               prop={'size': 8})
    plt.show()

    return fig
