import tkinter as tk
from tkinter import ttk, messagebox
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

        self.contenedor.rowconfigure(6, weight=1)


        

        self.labels()
        self.entry()
        self.buttons()
        self.combobox()
        self.table()

        self.cargar_datos()
        self.tabla.bind('<<TreeviewSelect>>', self.obtener_seleccion)


    def cargar_datos(self):
        usuario_activo = self.manejo_controller.controller_login.cliente_recibido.identificador
        
        self.entrada_dni.config(state='normal')
        self.entrada_dni.delete(0, tk.END)
        self.entrada_dni.insert(0,usuario_activo)
        self.entrada_dni.config(state='disabled')
        
    def labels(self):
        tk.Label(self.contenedor, text = '|Biblioteca Comunitaria CoopePuntarenas|', font = ('Arial',11,'bold'),bg='white').grid(row=0,column=0,sticky = 'we',columnspan=3,pady=20)

        tk.Label(self.contenedor, text = 'DNI:',bg='white').grid(row=1,column=0,sticky='w', padx = (30,0))

        tk.Label(self.contenedor, text = 'Libro Seleccionado:',bg='white').grid(row=2,column=0,sticky='w', padx = (30,0), pady = 5)

        tk.Label(self.contenedor, text = 'Filtrar por categoria: ',bg='white').grid(row=3,column=0, padx = (30,0), sticky = 'w', pady = 5)

        tk.Label(self.contenedor, text = 'Buscar por nombre: ',bg='white').grid(row=4,column=0, padx = (30,0), sticky = 'w', pady = 5)

    def buttons(self):
        self.btn_filtrar = tk.Button(self.contenedor, text = 'Filtrar',command = lambda: self.manejo_controller.cargar_filtrado_categoria(self))
        self.btn_filtrar.grid(row=3,column=2,sticky='e')

        self.btn_buscar = tk.Button(self.contenedor, text = 'Buscar',command = lambda: self.manejo_controller.cargar_filtrado_nombre(self))
        self.btn_buscar.grid(row=4, column = 2, sticky = 'e')


        self.btn_solicitar_prestamo = tk.Button(self.contenedor, text = 'Solicitar Prestamo', command = lambda: self.manejo_controller.registrar_prestamo(self))
        self.btn_solicitar_prestamo.grid(row=5, column = 0, sticky = 'nswe', columnspan=3)


    def entry(self):
        self.entrada_dni = tk.Entry(self.contenedor)
        self.entrada_dni.grid(row=1,column=1, sticky = 'we', padx = 5, columnspan = 1)
        self.entrada_dni.config(state = 'disabled')

        self.titulo_libro = tk.Entry(self.contenedor)
        self.titulo_libro.grid(row = 2, column = 1, padx = (100,0), pady = 5)
        self.titulo_libro.config(state = 'disabled')



        self.id_libro = tk.Entry(self.contenedor)
        self.id_libro.config(state = 'disabled')
        self.id_libro.grid(row = 2, column = 1, sticky = 'w', padx = 5, pady = 5)

        self.entry_barra_busqueda = tk.Entry(self.contenedor)
        self.entry_barra_busqueda.grid(row=4,column=1,sticky='we', padx = (5,10), pady = 5)

    def combobox(self):
        lista = ['Fantasia','Romance','Drama','Terror','Ciencia Ficcion','Historia','Infantil','Misterio','Suspenso']
        
        self.combobox = ttk.Combobox(self.contenedor, values = (lista), state = 'readonly')
        self.combobox.grid(row=3,column=1,sticky='we', padx = (5,10), pady = 5)
        self.combobox.set('seleccione')


    def table(self):
        columnas = ['Codigo','Autor','Titulo','Inventario']
        self.tabla = ttk.Treeview(self.contenedor, columns = columnas, show = 'headings')
        self.tabla.grid(row=6,column=0,columnspan=3,rowspan=4,sticky='nswe',pady=5)
        for items in columnas:
            self.tabla.heading(items, text = items)


    def obtener_seleccion(self, event):
        self.id_seleccionado = self.tabla.selection()
        if self.id_seleccionado:
            item = self.id_seleccionado[0]

            valores = self.tabla.item(item)['values']

            item_id = valores[0]
            titulo = valores[2]



            self.id_libro.config(state = 'normal')
            self.id_libro.delete(0, tk.END)
            self.id_libro.insert(0, item_id)
            self.id_libro.config(state = 'disabled')

            self.titulo_libro.config(state = 'normal')
            self.titulo_libro.delete(0, tk.END)
            self.titulo_libro.insert(0,titulo)
            self.titulo_libro.config(state = 'disabled')



    def insertar_tabla(self, arreglo):
        # self.id_libro = id_libro
        # self.titulo = titulo
        # self.autor = autor
        for items in arreglo:
            if items:
                id = items.id_libro
                autor = items.autor
                titulo = items.titulo
                inventario = items.inventario
                self.tabla.insert('',tk.END, values = (id,autor,titulo,inventario))

    def limpiar_tabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)


    def mostrar_adv(self, error):
        messagebox.showwarning('Advertencia',error, parent = self.ventana)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo('Informacion', mensaje, parent=self.ventana)