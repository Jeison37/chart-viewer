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

if __name__ == "__main__":
    unittest.main()