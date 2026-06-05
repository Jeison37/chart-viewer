import unittest
from csvreader import CSVReader 

class TestCSVReader(unittest.TestCase):

    def setUp(self):
        self.empty_reader = CSVReader()
        
        self.loaded_reader = CSVReader()
        self.loaded_reader.load_data("datos.csv")

    def test_load_data_success(self):
        res = self.empty_reader.load_data("datos.csv")
        self.assertTrue(res)
        self.assertIsNotNone(self.empty_reader._raw_data)

    def test_load_data_failure(self):
        res = self.empty_reader.load_data("fail.csv")
        self.assertFalse(res)
        self.assertIsNone(self.empty_reader._raw_data)

    def test_get_column_names(self):
        columns = self.loaded_reader.get_column_names()
        self.assertEqual(columns, ["Mes", "Ventas", "Gastos", "Nuevos_Clientes"])

    def test_get_column_names_empty(self):
        empty_columns = self.empty_reader.get_column_names()
        self.assertEqual(empty_columns, [])
if __name__ == "__main__":
    unittest.main()