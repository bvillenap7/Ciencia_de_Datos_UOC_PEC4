# This software is MIT licensed (see LICENSE)

import unittest
import pandas as pd
from Ejercicio_2_2 import crear_diccionario
import os
import shutil


class MyTestDicc(unittest.TestCase):

    directorio_principal = os.getcwd()

    def setUp(self):
        self.temp_dir = os.path.abspath(os.path.join
                                        (os.path.dirname(__file__),
                                         'directorio_temporal'))
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

    def test_dicc(self):

        datos_1 = {'id': [1, 2, 3],
                   'name': [1, 2, 3],
                   'homepage': ['Il Capo dei Capi', pd.NA, 'Fariña'],
                   'poster_path': ['A', 'B', 'C']}
        self.csv_1 = os.path.join(self.temp_dir, 'csv_1.csv')
        pd.DataFrame(datos_1).to_csv(self.csv_1, index=False)

        datos_2 = {'id': [1, 2, 3],
                   'name': [1, 2, 3],
                   'homepage': ['Il Capo dei Capi', 'Gomorra', ''],
                   'poster_path': ['A', pd.NA, 'C']}
        self.csv_2 = os.path.join(self.temp_dir, 'csv_2.csv')
        pd.DataFrame(datos_2).to_csv(self.csv_2, index=False)

        datos_3 = {'id': [1, 2, 3],
                   'name': [1, 2, 3],
                   'homepage': ['', 'Gomorra', 'Fariña'],
                   'poster_path': [pd.NA, 'B', 'C']}
        self.csv_3 = os.path.join(self.temp_dir, 'csv_3.csv')
        pd.DataFrame(datos_3).to_csv(self.csv_3, index=False)

        resultado = crear_diccionario(self.temp_dir)

        self.assertEqual(list(resultado.keys()), [1, 2, 3])
        self.assertEqual(resultado[1], ('NOT AVAILABLE', 'NOT AVAILABLE'))

    def tearDown(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    os.chdir(directorio_principal)
    

if __name__ == '__main__':
    unittest.main()
