# charts.py
import pandas as pd
from abc import ABC, abstractmethod

class Chart(ABC):
    def __init__(self, title="Gráfico", color_theme="#0ea5e9"):
        self._title = title 
        self._color_theme = color_theme 

    @abstractmethod
    def render(self, ax, data_x, data_y):
        pass

class BarChart(Chart):
    def render(self, ax, data_x, data_y):
        ax.clear()
        ax.axis("on") 
        ax.bar(data_x, data_y, color=self._color_theme) 
        ax.set_title(self._title, color="white")
        ax.tick_params(axis="x", rotation=45, colors="white") 
        ax.tick_params(axis="y", colors="white")
        ax.figure.tight_layout()

class LineChart(Chart):
    def render(self, ax, data_x, data_y):
        ax.clear()
        ax.axis("on") 
        ax.plot(data_x, data_y, color=self._color_theme, marker="o", linestyle="-") 
        ax.set_title(self._title, color="white")
        ax.tick_params(axis="x", rotation=45, colors="white")
        ax.tick_params(axis="y", colors="white")
        ax.figure.tight_layout()

class PieChart(Chart):
    def __init__(self, title="Gráfico", color_theme=None):
        if color_theme is None:
            color_theme = ["#0ea5e9", "#ec4899", "#8b5cf6", "#10b981", "#f59e0b", "#ef4444"]
        super().__init__(title, color_theme)

    def render(self, ax, data_x, data_y):
        ax.clear()
        ax.axis("off") 
        try:
            pd.to_numeric(data_y)
            valores = data_y
            etiquetas = data_x
        except ValueError:
            
            valores = data_x
            etiquetas = data_y

        ax.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=90, 
               colors=self._color_theme, textprops={"color": "white"})
               
        ax.set_title(self._title, color="white")
        ax.axis("equal")