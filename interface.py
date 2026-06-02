import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MainWindow(tb.Window):
    def __init__(self, data_handler):
        super().__init__(themename="superhero") 
        self.title("Visualizador CSV")
        self.geometry("900x600")

        self.data_handler = data_handler 

        self.current_chart = None 

        self.filepath_var = tb.StringVar(value="Ningún archivo CSV seleccionado...")

        self._build_interface()

    def _build_interface(self):
        controls_panel = tb.Frame(self, padding=15)
        controls_panel.pack(fill=X, side=TOP)

        btn_load = tb.Button(
            controls_panel, 
            text="Cargar CSV", 
            command=self.open_file_dialog, 
            bootstyle=SUCCESS
        )
        btn_load.pack(side=LEFT, padx=10)

        lbl_path = tb.Label(
            controls_panel, 
            textvariable=self.filepath_var, 
            font=("Helvetica", 10, "italic")
        )
        lbl_path.pack(side=LEFT, padx=10)

        self.grafic_panel = tb.Frame(self, padding=10)
        self.grafic_panel.pack(fill=BOTH, expand=YES)

        self.figure, self.ax = plt.subplots(figsize=(6, 4), dpi=100)
        self.figure.patch.set_facecolor('#0f172a')
        self.ax.set_facecolor('#1e293b')
        self.ax.tick_params(colors='white')
        
        self.ax.axis('off')
        
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.grafic_panel)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=YES)

    def open_file_dialog(self):
        path = filedialog.askopenfilename(
            title="Selecciona un archivo de datos",
            filetypes=[("Archivos CSV", "*.csv")]
        )
        
        if path:
            if self.data_handler.load_data(path):
                self.filepath_var.set(f"Archivo cargado: {path}")
                self.update_ui()

    def update_ui(self):
        pass