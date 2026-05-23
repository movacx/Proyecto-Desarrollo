import tkinter as tk
from tkinter import ttk, messagebox
#archivo: panel_book_view.py
class PanelLibros:
    def __init__(self, enlace_ventana, controller):
        self.controller = controller
        self.contenedor = tk.Frame(enlace_ventana)
        self.contenedor.pack(side='right',fill='both',expand=True)
        self._table()

    def _table(self):
        columnas = ['ID','Titulo','Autor','Inventario','Estante N°']
        self.tabla_libro = ttk.Treeview(self.contenedor, column = columnas, show = 'headings')
        self.tabla_libro.grid(row = 0, column = 0, sticky = 'nswe')

        for items in columnas:
            self.tabla_libro.heading(items, text = items)
