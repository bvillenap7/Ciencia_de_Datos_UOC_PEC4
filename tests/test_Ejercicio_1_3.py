# This software is MIT licensed (see LICENSE)

import unittest
import shutil
import os
import pandas as pd
from Ejercicio_1_3 import csv_to_df_bycsv


class TestCSVDataFramebyCSV(unittest.TestCase):

    # Creamos directorio temporal

    directorio_principal = os.getcwd()

    def setUp(self):
        self.temp_dir = os.path.abspath(os.path.join
                                        (os.path.dirname(__file__),
                                         'directorio_temporal'))
        os.makedirs(self.temp_dir)

    def test_csv_to_df_bycsv(self):
        # Creamos datos para realizar las pruebas
        dat_1 = {'id': [1, 2, 3], 'serie1': ['Il Capo dei Capi', 'Gomorra',
                                            'Fariña']}
        self.csv_1 = os.path.join(self.temp_dir, 'csv_1.csv')
        pd.DataFrame(dat_1).to_csv(self.csv_1, index=False)

        dat_2 = {'id': [1, 2, 3], 'serie2': ['Suburra', 'Roma Criminale',
                                            'Los Gambino']}
        self.csv_2 = os.path.join(self.temp_dir, 'csv_2.csv')
        pd.DataFrame(dat_2).to_csv(self.csv_2, index=False)

        dat_3 = {'id': [1, 2, 3], 'serie3': ['Los Soprano', 'Peaky Blinders',
                                            'Ndranghueta']}
        self.csv_3 = os.path.join(self.temp_dir, 'csv_3.csv')
        pd.DataFrame(dat_3).to_csv(self.csv_3, index=False)

        # Testeamos nuestra función
        tiempo, df_3 = csv_to_df_bycsv(self.temp_dir)
        num_columna = 3

        self.assertEqual(len(df_3), num_columna)
        self.assertLess(tiempo, 10.00)

    # Eliminamos el directorio temporal
    def tearDown(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    os.chdir(directorio_principal)


if __name__ == '__main__':
    unittest.main()
