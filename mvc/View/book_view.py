import tkinter as tk
from tkinter import ttk, messagebox

class PanelLibros:
    def __init__(self, enlace_ventana):
        self.contenedor = tk.Frame(enlace_ventana)
        self.contenedor.pack(side='right', fill = 'both', expand=True)
        self._table()

    def _table(self):#id_libro:str, titulo:str, autor:str, inventario:int, estado_prestamo:bool,id_estante
        columnas = ['ID','Titulo','Autor','Inventario','Estante N°']
        self.tabla_libro = ttk.Treeview(self.contenedor, column = columnas, show = 'headings')
        self.tabla_libro.grid(row = 0, column = 0, sticky = 'nswe')

        for items in columnas:
            self.tabla_libro.heading(items, text = items)
