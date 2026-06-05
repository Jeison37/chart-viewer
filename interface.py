import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from charts import BarChart, LineChart, PieChart

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

        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.figure.patch.set_facecolor('#0f172a')
        self.ax = self.figure.add_subplot(111)
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
            columnas_texto = self.data_handler.get_categorical_columns()
            columnas_numeros = self.data_handler.get_numeric_columns()

            if not hasattr(self, "panel_opciones"):
                self.panel_opciones = tb.Frame(self, padding=10)
                self.panel_opciones.pack(fill=X, before=self.grafic_panel)
                
                tb.Label(self.panel_opciones, text="Eje X:").pack(side=LEFT, padx=5)
                self.cb_x = tb.Combobox(self.panel_opciones, values=columnas_texto, state="readonly")
                self.cb_x.pack(side=LEFT, padx=5)
                            
                tb.Label(self.panel_opciones, text="Eje Y:").pack(side=LEFT, padx=5)
                self.cb_y = tb.Combobox(self.panel_opciones, values=columnas_numeros, state="readonly")
                self.cb_y.pack(side=LEFT, padx=5)
    
                tb.Label(self.panel_opciones, text="Tipo:").pack(side=LEFT, padx=5)
                self.cb_tipo = tb.Combobox(self.panel_opciones, values=["Barras", "Líneas", "Pastel"], state="readonly")
                self.cb_tipo.pack(side=LEFT, padx=5)
                self.cb_tipo.set("Barras") 

                btn_generar = tb.Button(self.panel_opciones, text="Dibujar Gráfico", command=self.draw_chart, bootstyle=INFO)
                btn_generar.pack(side=LEFT, padx=15)
            else:
                self.cb_x["values"] = columnas_texto
                self.cb_y["values"] = columnas_numeros
                self.cb_x.set("")
                self.cb_y.set("")

    def draw_chart(self):
        eje_x = self.cb_x.get()
        eje_y = self.cb_y.get()
        tipo = self.cb_tipo.get()

        if not eje_x or not eje_y:
            print("Por favor, selecciona ambos ejes.")
            return

        datos = self.data_handler.get_data_subset([eje_x, eje_y])

        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor("#1e293b")

        if tipo == "Barras":
            self.current_chart = BarChart(title=f"{eje_y} por {eje_x}")
        elif tipo == "Líneas":
            self.current_chart = LineChart(title=f"Tendencia de {eje_y}")
        elif tipo == "Pastel":
            self.current_chart = PieChart(title=f"Distribución de {eje_y}")
            
        self.current_chart.render(self.ax, datos[eje_x], datos[eje_y])

        self.canvas.draw()