import tkinter as tk
from tkinter import ttk
class PrestamoUsuario:
    def __init__(self, enlace_ventana, controller):
        self.manejo_controller = controller
        self.ventana = enlace_ventana
        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.pack(side='right',fill='both',expand=True)
        self.contenedor.configure(bg='white')

        self.contenedor.columnconfigure(0,weight=0)
        self.contenedor.columnconfigure(1,weight=1)
        self.contenedor.columnconfigure(2, weight=0)

        self.contenedor.rowconfigure(5, weight=1)


        self.forms()
        self.table()


    def forms(self):
        tk.Label(self.contenedor, text = '|Biblioteca Comunitaria CoopePuntarenas|', font = ('Arial',11,'bold'),bg='white').grid(row=0,
                                                                                                                      column=0,
                                                                                                                      sticky = 'we',
                                                                                                                      columnspan=3,
                                                                                                                      pady=20)

        tk.Label(self.contenedor, text = 'DNI:',bg='white').grid(row=1,column=0,sticky='w', padx = (30,0))
        self.entrada_dni = tk.Entry(self.contenedor)
        self.entrada_dni.grid(row=1,column=1, sticky = 'we', padx = 5, columnspan = 1)
        self.entrada_dni.config(state = 'disabled')

        tk.Label(self.contenedor, text = 'Libro Seleccionado:',bg='white').grid(row=2,column=0,sticky='w', padx = (30,0), pady = 5)
        self.titulo_libro = tk.Entry(self.contenedor)
        self.id_libro = tk.Entry(self.contenedor)
        self.id_libro.config(state = 'disabled')
        self.id_libro.grid(row = 2, column = 1, sticky = 'w', padx = 5, pady = 5)
        self.titulo_libro.grid(row = 2, column = 1, padx = (0,500), pady = 5)
        self.titulo_libro.config(state = 'disabled')


        lista = ['Fantasia','Romance','Drama','Terror','Ciencia Ficcion','Historia','Infantil','Misterio','Suspenso']
        tk.Label(self.contenedor, text = 'Filtrar por categoria: ',bg='white').grid(row=3,column=0, padx = (30,0), sticky = 'w', pady = 5)
        self.combobox = ttk.Combobox(self.contenedor, values = (lista), state = 'readonly')
        self.combobox.grid(row=3,column=1,sticky='we', padx = (5,10), pady = 5)
        self.combobox.set('seleccione')

        tk.Label(self.contenedor, text = 'Buscar por nombre: ',bg='white').grid(row=4,column=0, padx = (30,0), sticky = 'w', pady = 5)
        self.filtrar_titulo = tk.Entry(self.contenedor)
        self.filtrar_titulo.grid(row=4,column=1,sticky='we', padx = (5,10), pady = 5)


    def table(self):
        columnas = ['Codigo','Autor','Titulo','']
        self.tabla = ttk.Treeview(self.contenedor, columns = columnas, show = 'headings')
        self.tabla.grid(row=5,column=0,columnspan=3,rowspan=4,sticky='nswe')
        for items in columnas:
            self.tabla.heading(items, text = items)