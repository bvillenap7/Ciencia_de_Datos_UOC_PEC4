# This software is MIT licensed (see LICENSE)
import os
from Ejercicio_1_2 import csv_to_dataframe
from Ejercicio_1_3 import csv_to_df_bycsv


def respuesta(ruta=None):
    """
    Esta función devuelve un analisis sobre la comparativa
    entre usar la librería pandas y la librería CSV a la hora
    de tratar un archivo de 10 GB

    """

    if ruta is None:
        ruta_1 = os.path.join(os.getcwd(), 'data')
        t1, df1 = csv_to_dataframe(ruta_1)
        t2, df2 = csv_to_df_bycsv(ruta_1)
    else:
        t1, df1 = csv_to_dataframe(ruta)
        t2, df2 = csv_to_df_bycsv(ruta)


    texto = ('En la lectura de los ficheros, siguiendo ambos métodos, '
             'se observa que hay una diferencia considerable en el tiempo '
             'de ejecución entre ambas funciones.\nEl tiempo de ejecucíon '
             f'de la función del apartado 1.2 usando pandas es de {round(t1, 4)} '
             'segundos.\n''El tiempo de ejecución de la función del apartado '
             f'1.3 usando CSV es de {round(t2, 4)} segundos.\nEsto en parte '
             'se debe a que la librería pandas está altamente optimizada y '
             'está escrita en C, lo que la hace más eficiente en términos '
             'de velocidad para manejar grandes volúmenes de datos.\n'
             'Teniendo en cuenta esto, podemos confirmar que el método que '
             'usa pandas sería más rápido para manejar archivos de 10GB. ')

    return print(texto)
