import tkinter as tk
from tkinter import ttk, messagebox
class AdministradorLibros:
    def __init__(self, enlace,controller):
        self.manejo_controller = controller
        self.contenedor = tk.Frame(enlace)
        self.contenedor.pack(side='right', fill='both', expand=True)
        self.contenedor.configure(bg='white')

        self.contenedor.columnconfigure(0, weight=0)
        self.contenedor.columnconfigure(1, weight=1)
        self.contenedor.columnconfigure(2, weight=0)
        self.contenedor.rowconfigure(5,weight=1)

        self.labels()
        self.table()
        self.forms()
        self.buttons()

        self.cargar()

        #Evento
        self.tabla.bind('<<TreeviewSelect>>', self.obtener_seleccion)

        # "Donación N°": 1634,
        # "Cliente": "604800208",
        # "Fecha de donación": "2026-05-22",
        # "Titulo del libro": "Los juegos del hambre",
        # "Nombre del autor": "Suzanne Collins",
        # "Cantidad donada": 12,
        # "Estado": false

        # self.desbloquear_botones()


    def cargar(self):
        self.manejo_controller.recibir_registros(self)

    def separador(self, x,y):
        tk.Label(self.contenedor, text='',bg='white').grid(row=x,column=y)

    def labels(self):
        tk.Label(self.contenedor, text = 'Gestor de libros', font = ('Arial',11,'bold'),bg='white').grid(row=0,column=0,columnspan=3,pady=10)
        tk.Label(self.contenedor, text = 'Id: ',bg='white').grid(row=1,column=0,sticky='w')
        tk.Label(self.contenedor, text = 'Filtrar por cliente: ',bg='white').grid(row=2,column=0,sticky='w')
        tk.Label(self.contenedor, text = 'Categoria a registrar:',bg='white').grid(row=1,column=1, sticky = 'e')
        self.entry_id = tk.Entry(self.contenedor)
        self.entry_id.grid(row=1,column=1, sticky='w')
        self.entry_id.config(state='disabled')

        self.entry_cliente = tk.Entry(self.contenedor)
        self.entry_cliente.grid(row=2,column=1, sticky='w')

        # self.separador(2,0)
        # self.separador(3,0)

    
    def forms(self):
        lista = ['Fantasia','Romance','Drama','Terror','Ciencia Ficcion','Historia','Infantil','Misterio','Suspenso']
        self.lista_opciones = ttk.Combobox(self.contenedor,state='readonly')
        self.lista_opciones['values']=lista
        self.lista_opciones.set('Seleccione')
        self.lista_opciones.grid(row=1,column=2,padx=10)

    def table(self):
        columnas = ["Donación N°","Cliente","Titulo del libro","Cantidad donada","Fecha de donación"]
        self.tabla = ttk.Treeview(self.contenedor, columns=columnas, show = 'headings')
        self.tabla.grid(row=5,column=0,columnspan=4,rowspan=5,sticky='nswe')

        for items in columnas:
            self.tabla.heading(items, text = items)

    def insertar_tabla(self, arreglo, valor):
        for items in arreglo:
            if valor == 0:
                if items.recibido == False:
                    id = items.id_donacion
                    cliente = items.id_cliente
                    titulo = items.titulo_libro
                    cant = items.cant_libros_donados
                    fecha = items.fecha_donacion
                    self.tabla.insert('',tk.END, values = (id,cliente,titulo,cant,fecha))
            else:
                if items.recibido == True:
                    id = items.id_donacion
                    cliente = items.id_cliente
                    titulo = items.titulo_libro
                    cant = items.cant_libros_donados
                    fecha = items.fecha_donacion
                    self.tabla.insert('',tk.END, values = (id,cliente,titulo,cant,fecha))



    def buttons(self):
        self.btn_enviar = tk.Button(self.contenedor, text = 'Registrar',command = lambda: self.manejo_controller.registrar_donacion())
        self.btn_enviar.grid(row=2,column=2,padx=10,pady=15)

        self.btn_buscar = tk.Button(self.contenedor, text = 'Filtrar', command = lambda: self.manejo_controller.cargar_filtrado_cliente())
        self.btn_buscar.grid(row=2,column=1, sticky='w', padx = (180,0))

        self.btn_eliminar = tk.Button(self.contenedor, text = 'Rechazar', command = lambda: self.manejo_controller.rechazar_donacion())
        self.btn_eliminar.grid(row=2,column=2, sticky = 'e', padx = (0,200))

    def obtener_seleccion(self, event):
        self.id_seleccionado = self.tabla.selection()
        if self.id_seleccionado:
            item = self.id_seleccionado[0]

            valores = self.tabla.item(item)['values']

            item_id = valores[0]

            self.entry_id.config(state='normal')
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0,item_id)
            self.entry_id.config(state='disabled')


    def limpiar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
    
    def limpiar_formulario(self):
        self.entry_cliente.delete(0, tk.END)
        self.lista_opciones.set('Seleccione')

    def bloquear_botones(self):
        self.btn_enviar.config(state='disabled')

    def desbloquear_botones(self):
        self.btn_enviar.config(state='normal')



    def mostrar_adv(self, error):
        messagebox.showwarning('Advertencia',error, parent = self.ventana)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo('Informacion', mensaje, parent=self.ventana)