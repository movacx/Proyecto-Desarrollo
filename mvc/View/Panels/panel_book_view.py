import tkinter as tk
from tkinter import ttk, messagebox
#archivo: panel_book_view.py
class PanelLibros:
    def __init__(self, enlace_ventana, controller):
        self.controller = controller
        self.contenedor = tk.Frame(enlace_ventana)
        self.contenedor.pack(side='right',fill='both',expand=True)

        self.contenedor.configure(bg='white')

        self.contenedor.columnconfigure(0,weight=0)
        self.contenedor.columnconfigure(1, weight = 1)
        self.contenedor.columnconfigure(2, weight=0)
        self.contenedor.rowconfigure(3,weight=1)
        
        self.cargar_pantalla()


    def cargar_pantalla(self):
        tk.Label(self.contenedor, text = '|Biblioteca Comunitaria CoopePuntarenas - Libros|', font = ('Arial',11,'bold'),bg='white').grid(row=0,
                                                                                                                      column=0,
                                                                                                                      sticky = 'we',
                                                                                                                      columnspan=3,
                                                                                                                      pady=20)
        tk.Label(self.contenedor, text = 'Buscar Libro: ',bg='white').grid(row=1,column=0, padx = (30,0), sticky = 'w')

        self.entry_barra_busqueda = tk.Entry(self.contenedor,width=20)
        self.entry_barra_busqueda.grid(row = 1, column = 1, sticky = 'we', padx = (5,10))


        lista = ['Fantasia','Romance','Drama','Terror','Ciencia Ficcion','Historia','Infantil','Misterio','Suspenso']
        tk.Label(self.contenedor, text = 'Filtrar por categoria: ',bg='white').grid(row=2,column=0, padx = (30,0), sticky = 'w')
        self.combobox = ttk.Combobox(self.contenedor, values = (lista), state = 'readonly')
        self.combobox.grid(row=2,column=1,sticky='we', padx = (5,10))
        self.combobox.set('seleccione')

        self.boton_buscar = tk.Button(self.contenedor, text = 'Buscar',
                                        bg="#3F4949",
                                        fg = 'white',
                                        font = ('Arial', 8, 'bold'),
                                        bd=0,
                                        padx = 15,
                                        pady = 8,
                                        anchor = 'w')
        self.boton_buscar.grid(row=1,column=2,sticky='w', padx = (0,5), pady = 5)

        columnas = ['ID','Titulo','Autor','Inventario','Estante N°']
        self.tabla_libro = ttk.Treeview(self.contenedor, column = columnas, show = 'headings')
        self.tabla_libro.grid(row = 3, column = 0, sticky = 'nswe',columnspan=3,rowspan=3,pady = 10, padx = (5,5))


        self.btn_filtrar = tk.Button(self.contenedor, text = 'Filtrar🔎',
                                        bg="#3F4949",
                                        fg = 'white',
                                        font = ('Arial', 8, 'bold'),
                                        bd=0,
                                        padx = 15,
                                        pady = 8,
                                        anchor = 'w')
        self.btn_filtrar.grid(row=2,column=2,sticky='w', padx = (0,5), pady = 5)

        for items in columnas:
            self.tabla_libro.heading(items, text = items)



