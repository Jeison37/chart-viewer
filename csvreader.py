import pandas as pd

class CSVReader:
    def __init__(self):
        self._raw_data = None 
        self._filepath = ""

    def load_data(self, filepath):
        try:
            self._raw_data = pd.read_csv(filepath)
            self._filepath = filepath
            return True
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            return False

    def get_column_names(self):
        if self._raw_data is not None:
            return self._raw_data.columns.tolist()
        return []

    def get_data_subset(self, columns):
        if self._raw_data is not None:
            return self._raw_data[columns].copy()
        return None