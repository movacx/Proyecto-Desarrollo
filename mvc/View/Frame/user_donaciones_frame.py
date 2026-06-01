import tkinter as tk
from tkinter import ttk
#archivo panel_donacion_view,py
class DonativoView:
    def __init__(self, enlace,controller):
        self.manejo_controller = controller
        self.contenedor = tk.Frame(enlace)
        self.contenedor.pack(side='right', fill = 'both', expand=True)

        self.contenedor.columnconfigure(0, weight=0)
        self.contenedor.columnconfigure(1, weight=1)
        self.contenedor.columnconfigure(2, weight=0)
        self.contenedor.rowconfigure(6, weight=1)

        self.contenedor.configure(bg='white')

        self._labels()
        self._entry()
        self._buttons()
        self._table()

        

        self._insertar_dni(self.manejo_controller.controller_login.cliente_recibido.identificador)
        self.entry_dni_cliente.config(state='disabled')

        self.cargar()


    def cargar(self):
        self.manejo_controller.recibir_registros(self)

    def _labels(self):
        tk.Label(self.contenedor, text = '|Biblioteca Comunitaria CoopePuntarenas - Donar Libros|', font = ('Arial',11,'bold'),bg='white').grid(row=0,
                                                                                                                      column=0,
                                                                                                                      sticky = 'we',
                                                                                                                      columnspan=2,
                                                                                                                      pady=20)
        # self.id_donacion = id_donacion
        # self.fecha_donacion = fecha_donacion
        # self.id_cliente = id_cliente
        # self.nombre_autor = nombre_autor
        # self.titulo_libro = titulo_libro

        tk.Label(self.contenedor, text = 'Cedula del cliente: ',bg='white').grid(row=1, column=0,sticky='w',pady=10,padx=30)
        tk.Label(self.contenedor, text = 'Titulo del libro a donar: ',bg='white').grid(row=2, column=0,sticky='w',pady=10,padx=30)
        tk.Label(self.contenedor, text = 'Nombre del autor: ',bg='white').grid(row=3, column=0,sticky='w',pady=10,padx=30)
        tk.Label(self.contenedor, text = 'Cantidad a donar: ',bg='white').grid(row=4, column=0,sticky='w',pady=10,padx=30)

        tk.Label(self.contenedor, text = ' ').grid(row = 0, column = 2)
    
    def _entry(self):
        self.entry_dni_cliente = tk.Entry(self.contenedor, width=80)
        self.entry_dni_cliente.grid(row=1, column=1,sticky='we')

        self.entry_titulo = tk.Entry(self.contenedor,width=80)
        self.entry_titulo.grid(row=2,column=1,sticky='we')

        self.entry_nombre_autor = tk.Entry(self.contenedor,width=80)
        self.entry_nombre_autor.grid(row=3,column=1,sticky='we')

        self.entry_cantidad = tk.Entry(self.contenedor,width=80)
        self.entry_cantidad.grid(row=4,column=1,sticky='we')


    def _buttons(self):
        self.enviar = tk.Button(self.contenedor, text = 'Entregar Libro',
                                bg = "#0E0909",
                                fg = "#FFFFFF",
                                bd=0,
                                command = lambda: self.manejo_controller.donar_libro())
        
        self.enviar.grid(row = 5, column =0, columnspan = 2,pady = 20)

    def _table(self):
        columnas = ['Donativo N°','Autor','Titulo','Cantidad','Estado']
        self.tabla = ttk.Treeview(self.contenedor, columns=columnas, show = 'headings')
        self.tabla.grid(row = 6, column = 0, sticky = 'nswe',columnspan = 2, rowspan=6)

        for items in columnas:
            self.tabla.heading(items, text = items)

    def insertar_tabla(self, arreglo):
        _estado = 'Pendiente' #id_donacion:str, id_cliente:str, fecha_donacion:str, nombre_autor:str, titulo_libro:str, cant_libros_donados:int, recibido:bool
        for items in arreglo:
            id = items.id_donacion
            autor = items.nombre_autor
            titulo = items.titulo_libro
            cant = items.cant_libros_donados
            estado = items.recibido

            if estado == False:
                _estado = 'Pendiente'
            else:
                _estado = 'Recibido y procesado'


            self.tabla.insert('',tk.END, values = (id,autor,titulo,cant,_estado))

    def limpiar_tabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)

    def limpiar_campos(self):
        self.entry_cantidad.delete(0, tk.END)
        self.entry_nombre_autor.delete(0, tk.END)
        self.entry_titulo.delete(0, tk.END)

    def _insertar_dni(self, dni):
        self.entry_dni_cliente.delete(0, tk.END)
        self.entry_dni_cliente.insert(0, dni)

