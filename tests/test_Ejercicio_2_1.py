# This software is MIT licensed (see LICENSE)

import unittest
from Ejercicio_2_1 import add_days
import os
import shutil
import pandas as pd

class TestAddDays(unittest.TestCase):

    directorio_principal = os.getcwd()

    def setUp(self):
        self.temp_dir = os.path.abspath(os.path.join
                                        (os.path.dirname(__file__),
                                         'directorio_temporal'))
        os.makedirs(self.temp_dir)
    def test_add_days(self):

        datos_1 = {'id': [1, 2, 3],
                   '': [1, 2, 3],
                   'last_air_date': ['1991', '1982', '1973'],
                   'first_air_date': ['2000', '2010', '2020']}
        self.csv_1 = os.path.join(self.temp_dir, 'csv_1.csv')
        pd.DataFrame(datos_1).to_csv(self.csv_1, index=False)

        datos_2 = {'id': [1, 2, 3],
                   'name': [1, 2, 3],
                   'last_air_date': ['1991', '1920', '1910'],
                   'first_air_date': ['1990', '1980', '1970']}
        self.csv_2 = os.path.join(self.temp_dir, 'csv_2.csv')
        pd.DataFrame(datos_2).to_csv(self.csv_2, index=False)

        datos_3 = {'id': [1, 2, 3],
                   'name': [1, 2, 3],
                   'last_air_date': ['1290', '1480', '1570'],
                   'first_air_date': ['1960', '1950', '1940']}
        self.csv_3 = os.path.join(self.temp_dir, 'csv_3.csv')
        pd.DataFrame(datos_3).to_csv(self.csv_3, index=False)

        resultado = add_days(self.temp_dir)
        self.assertGreaterEqual(len(resultado), 3)

    def tearDown(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    os.chdir(directorio_principal)

if __name__ == '__main__':
    unittest.main()
