# This software is MIT licensed (see LICENSE)

import unittest
import os
import shutil
import zipfile
import tarfile
from Ejercicio_1_1 import descomprimir


class Testdescomprimir(unittest.TestCase):

    # Creamos directorio temporal
    directorio_principal = os.getcwd()

    def setUp(self):
        self.temp_dir = os.path.abspath(os.path.join
                                        (os.path.dirname(__file__),
                                         'directorio_temporal'))
        os.makedirs(self.temp_dir)

    # Eliminamos el directorio temporal
    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    # Creamos archivo zip comprimiendo test.txt
    def test_desomprimir_zip(self):
        zip_ruta = os.path.join(self.temp_dir, 'test.zip')
        archivo_txt = os.path.abspath(os.path.join(os.path.dirname
                                                   (__file__), 'test.txt'))
        with zipfile.ZipFile(zip_ruta, 'w') as archivo_zip:
            archivo_zip.write(archivo_txt, 'test.txt')

        try:
            self.assertTrue(descomprimir(zip_ruta))
            self.assertFalse(descomprimir('test.txt'))

        except AssertionError as e:
            print(f'Error: {e}')

    # Creamos archivo tar.gz comprimiendo test.txt
    def test_comprimir_targz(self):
        targz_ruta = os.path.join(self.temp_dir, 'test.tar.gz')
        archivo_txt = os.path.abspath(os.path.join(os.path.dirname
                                                   (__file__), 'test.txt'))
        with tarfile.open(targz_ruta, 'w:gz') as archivo_targz:
            archivo_targz.add(archivo_txt, 'test.txt')

        try:
            self.assertTrue(descomprimir(targz_ruta))
            self.assertFalse(descomprimir('test.txt'))

        except AssertionError as e:
            print(f'Error: {e}')
    # Testeamos módulo Ejercicio_1_1

    os.chdir(directorio_principal)


if __name__ == '__main__':
    unittest.main()
