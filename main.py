from csvreader import CSVReader

if __name__ == "__main__":
    lector = CSVReader()
    if lector.load_data("datos.csv"): 
        columnas = lector.get_column_names()
        print(f"Las columnas disponibles son: {columnas}")