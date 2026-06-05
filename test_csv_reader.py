import unittest
from csvreader import CSVReader 

class TestCSVReader(unittest.TestCase):
    
    def test_load_data_success(self):
        reader = CSVReader()
        res = reader.load_data("datos.csv")
        
        self.assertTrue(res)
        self.assertIsNotNone(reader._raw_data)

    def test_load_data_failure(self):
        reader = CSVReader()
        res = reader.load_data("fail_test.csv")
        
        self.assertFalse(res)
        self.assertIsNone(reader._raw_data)

    def test_get_column_names(self):
        reader = CSVReader()
        reader.load_data("datos.csv")
        
        columns = reader.get_column_names()
        self.assertEqual(columns, ["Mes", "Ventas", "Gastos", "Nuevos_Clientes"])

    def test_get_column_names_empty(self):
        reader = CSVReader()
        empty_columns = reader.get_column_names()
        
        self.assertEqual(empty_columns, [])
if __name__ == "__main__":
    unittest.main()