# This software is MIT licensed (see LICENSE)

import unittest
import pandas as pd
import os
import shutil
from Ejercicio_4_1 import grafico_by_year
import matplotlib


class MyTestshow(unittest.TestCase):

    directorio_principal = os.getcwd()

    def setUp(self):
        self.temp_dir = os.path.abspath(os.path.join
                                        (os.path.dirname(__file__),
                                         'directorio_temporal'))
        os.makedirs(self.temp_dir)

    def test_grafico(self):

        dat_1 = {'id': [1, 2, 3], 'first_air_date': ['1997', '1998', '1999']}
        self.csv_1 = os.path.join(self.temp_dir, 'csv_1.csv')
        pd.DataFrame(dat_1).to_csv(self.csv_1, index=False)

        dat_2 = {'id': [1, 2, 3], 'original_name': ['Fargo', 'Peaky', 'Star']}
        self.csv_2 = os.path.join(self.temp_dir, 'csv_2.csv')
        pd.DataFrame(dat_2).to_csv(self.csv_2, index=False)

        dat_3 = {'id': [1, 2, 3], 'name': ['HBO', 'Mov', 'Amz']}
        self.csv_3 = os.path.join(self.temp_dir, 'csv_3.csv')
        pd.DataFrame(dat_3).to_csv(self.csv_3, index=False)

        n = grafico_by_year(self.temp_dir)
        self.assertEqual(type(n), matplotlib.figure.Figure)

    def tearDown(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    os.chdir(directorio_principal)


if __name__ == '__main__':
    unittest.main()
