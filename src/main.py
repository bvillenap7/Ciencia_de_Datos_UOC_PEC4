# This software is MIT licensed (see LICENSE)

from Ejercicio_1_1 import descomprimir
from Ejercicio_1_2 import csv_to_dataframe
from Ejercicio_1_3 import csv_to_df_bycsv
from Ejercicio_1_4 import respuesta
from Ejercicio_2_1 import add_days
from Ejercicio_2_2 import crear_diccionario
from Ejercicio_3_1 import show
from Ejercicio_3_2 import cancel
from Ejercicio_3_3 import japones
from Ejercicio_4_1 import grafico_by_year
from Ejercicio_4_2 import grafico_by_decade
from Ejercicio_4_3 import grafico_circular
from Ejercicio_5 import analisis


if __name__ == '__main__':

    print('******************************************\n'
          '**** INICIO DE EJECUCIÓN DEL PROGRAMA ****\n'
          '******************************************')

    print('Implementamos nuestra función para descomprimir los archivos.zip o .tar.gz')
    Ej_1_1 = descomprimir(input('Escriba la ruta absoluta del archivo que desea descomprimir incluyendo'
                                'el nombre del archivo y su extensión:\n'))
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print('\nImplementamos nuestra función para crear un DataFrame con el contenido de los archivos '
          'descomprimidos usando la librería Pandas.')
    ruta = input('Escriba la ruta absoluta donde se encuentren los archivos CSV '
          'descomprimidos:\n')
    Ej_1_2 = csv_to_dataframe(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print('\nImplementamos nuestra función para crear un DataFrame con el contenido de los archivos '
          'descomprimidos usando la librería CSV.')
    Ej_1_3 = csv_to_df_bycsv(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    Ej_1_4 = respuesta(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print('\nImplementamos una función que añade la variable air_days al dataframe. La nueva variable contiene el '
          'número de días que una serie ha estado en emisión.\nMostramos por pantalla los 10 registros del dataset '
          'que más días han estado en emisión.')
    Ej_2_1 = add_days(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print('\nImplementamos una función que crea un diccionario ordenado cuya clave será el nombre de la serie (name) y '
          'cuyo valor será la dirección web completa de su poster (homepage y poster_path). En caso de que homepage o '
          'poster_path tengan el valor NaN o "", el valor será el string “NOT AVAILABLE”.\nMostramos por pantalla los '
          'primeros 5 registros del diccionario:')
    Ej_2_2 = crear_diccionario(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print('\nImplementamos una función que obtiene y muestra por pantalla los nombres de las series cuyo idioma original '
          '(original_language) es el inglés y en cuyo resumen (overview) aparecen las palabras “mystery” o “crime”, '
          'sin tener en cuenta mayúsculas ni minúscula.')
    Ej_3_1 = show(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print('\nImplementamos una función que obtiene una lista de las series que han empezado en 2023 y han sido '
          'canceladas.\n Mostramos por pantalla los primeros 20 elementos de esta lista.')
    Ej_3_2 = cancel(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print('\nImplementamos una función que obtiene un dataframe con los nombres, los nombres originales, las '
          'plataformas de emisión y las empresas productoras de todas las series cuyo idioma (variable languages) '
          'es el japonés.\nMostramos los primeros 20 registros por pantalla.\nNota: tened en cuenta que consideramos '
          'series en japonés también aquellas que tienen idiomas adicionales, por ejemplo, un registro con idioma '
          '“en, ja, ko” estará incluido.')
    Ej_3_3 = japones(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print('\nImplementamos una función que muestra en un gráfico de barras el número de series por año de inicio. '
          '\nNOTA: CIERRE LA GRÁFICA PARA QUE EL PROGRAMA PUEDA CONTINUAR.')
    Ej_4_1 = grafico_by_year(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print('\nImplementamos una función que crea un gráfico de líneas que muestra el número de series de cada '
          'categoría de la variable “type” producidas en cada década desde 1940.\nEn esta gráfica podemos observar,'
          'un incremento exponencial muy llamativo por los programas guionizados, y a su vez, podemos ver un cambio '
          'de tendencia a partir de 2020, dónde todos los registros descienden en términos generales.\n'
          'NOTA: CIERRE LA GRÁFICA PARA QUE EL PROGRAMA PUEDA CONTINUAR.')
    Ej_4_2 = grafico_by_decade(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print('\nImplementemos una función que obtiene el número de series por género y muestra el porcentaje respecto '
          'al total en un gráfico circular. Los géneros que representen menos del 1% del total se incluyen en la '
          'categoría "Other". Aquella serie que tenga más de un género se incluye en todas las categorías en que '
          'esté clasificada.\nNota: Las series con el campo "genres" vacío no se incluyen. Amplie el gráfico en su '
          'totalidad para poder visualizar la leyenda, la cual contiene los porcentajes asociados a cada género. '
          '\nNOTA: CIERRE LA GRÁFICA PARA QUE EL PROGRAMA PUEDA CONTINUAR')
    Ej_4_3 = grafico_circular(ruta)
    input('\nPULSE ENTER PARA CONTINUAR\n')

    print()
    Ej_5 = analisis()
    print('***************************************\n'
          '**** FIN DE EJECUCIÓN DEL PROGRAMA ****\n'
          '***************************************')
