# This software is MIT licensed (see LICENSE)

import os
from Ejercicio_1_2 import csv_to_dataframe


def japones(ruta=None):
    """
    Esta función obtiene un dataframe con los nombres,
    los nombres originales, las plataformas de emisión
    y las empresas productoras de todas las series cuyo
    idioma (variable languages) sea el japonés.

    A su vez, muestra los primeros 20 registros
    por pantalla.

    Nota: tened en cuenta que consideramos
    series en japonés también aquellas que tengan idiomas
    adicionales, por ejemplo, un registro con idioma
    “en, ja, ko” se incluiría.

    """

    if ruta is None:
        ruta_1 = os.path.join(os.getcwd(), 'data')
        t1, dataframe = csv_to_dataframe(ruta_1)
    else:
        t1, dataframe = csv_to_dataframe(ruta)

    df_japon = dataframe[dataframe['languages'].astype(str).str.contains('ja|ja,')][
        ['name', 'original_name', 'networks', 'production_companies', 'languages']
    ]

    print(df_japon.head(20))

    return df_japon
