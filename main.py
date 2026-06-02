from csvreader import CSVReader
from interface import MainWindow

if __name__ == "__main__":

    reader = CSVReader()

    app = MainWindow(data_handler=reader)

    app.mainloop()