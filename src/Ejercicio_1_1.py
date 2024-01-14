# This software is MIT licensed (see LICENSE)

import os
import zipfile
import tarfile


def descomprimir(ruta) -> bool:
    """
    Función que descomprime ficheros
    en formato zip y tar.gz. La función recibe como
    inputs la ruta con el nombre del fichero que se quiere
    descomprimir. La función detectará automáticamente
    si el fichero está comprimido en zip o en tar.gz y
    mostrará un mensaje de error cuando el fichero sea
    de otro tipo. Utilizad esta función para descomprimir
    el fichero TMDB.zip.
    """

    directorio_principal = os.getcwd()

    try:
        ruta_directorio = os.path.dirname(ruta)
        if ruta_directorio:
            os.chdir(ruta_directorio)

        _, extension = os.path.splitext(ruta)

        if extension == '.zip':
            if os.path.exists(ruta):
                with zipfile.ZipFile(ruta, 'r') as archivo_zip:
                    archivo_zip.extractall('.')
                return True
            else:
                print(f'Error: La ruta {ruta} es errónea')
                return False
        elif extension == '.gz' or extension == '.tar.gz':
            if os.path.exists(ruta):
                with tarfile.open(ruta, 'r:gz') as archivo_targz:
                    archivo_targz.extractall('.')
                return True
            else:
                print(f'Error: La ruta {ruta} es errónea')
                return False
        else:
            print(f'Error: El archivo {ruta} no está en formato zip o tar.gz')
            return False

    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        os.chdir(directorio_principal)


'''
descomprimir('C:/Users/bvill/Documents/4. UOC/1º Programación '
             'para Ciencia de Datos/PEC 4/Entregable/activity_4'
             '/PEC4_Borja Villena Pardo/data/TMDB.zip')
'''
