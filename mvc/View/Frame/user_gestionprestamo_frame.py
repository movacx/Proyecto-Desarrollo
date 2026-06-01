import tkinter as tk
from tkinter import ttk, messagebox
class DevolverPrestamo:
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
        self.table()

        self.cargar_datos()
        self.tabla.bind('<<TreeviewSelect>>', self.obtener_seleccion)

        self.cargar()
        
    def cargar(self):
        self.limpiar_tabla()
        self.manejo_controller.listar_prestamos(self)


    def cargar_datos(self):
        usuario_activo = self.manejo_controller.controller_login.cliente_recibido.identificador
        
        self.entrada_dni.config(state='normal')
        self.entrada_dni.delete(0, tk.END)
        self.entrada_dni.insert(0,usuario_activo)
        self.entrada_dni.config(state='disabled')
        
    def labels(self):
        tk.Label(self.contenedor, text = '|Biblioteca Comunitaria CoopePuntarenas|', font = ('Arial',11,'bold'),bg='white').grid(row=0,column=0,sticky = 'we',columnspan=3,pady=20)

        tk.Label(self.contenedor, text = 'DNI:',bg='white').grid(row=1,column=0,sticky='w', padx = (30,0))

        tk.Label(self.contenedor, text = 'Prestamo Seleccionado:',bg='white').grid(row=2,column=0,sticky='w', padx = (30,0), pady = 5)


    def buttons(self):
        self.btn_devoler_prestamo = tk.Button(self.contenedor, text = 'Devolver Libro',
                                              command = lambda: self.manejo_controller.accion_devolver_libro(self))
        self.btn_devoler_prestamo.grid(row=5, column = 0, sticky = 'nswe', columnspan=3)


    def entry(self):
        self.entrada_dni = tk.Entry(self.contenedor)
        self.entrada_dni.grid(row=1,column=1, sticky = 'we', padx = 5, columnspan = 1)
        self.entrada_dni.config(state = 'disabled')

        self.id_prestamo = tk.Entry(self.contenedor)
        self.id_prestamo.config(state = 'disabled')
        self.id_prestamo.grid(row = 2, column = 1, sticky = 'we', padx = 5, pady = 5, columnspan = 1)


    def table(self):
        columnas = ['Prestamo N°','Libro','Fecha Limite de devolucion','Estado Prestamo']
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

            self.id_prestamo.config(state = 'normal')
            self.id_prestamo.delete(0, tk.END)
            self.id_prestamo.insert(0, item_id)
            self.id_prestamo.config(state = 'disabled')

    def insertar_tabla(self, arreglo):
        for items in arreglo:
            if items:
                id = items.id_prestamo
                id_libro = items.id_libro
                fecha_d = items.fecha_devolucion

                if items.estado == True:
                    estado = 'Activo'
                if items.estado == False:
                    estado = 'Devuelto'


                self.tabla.insert('',tk.END, values = (id,id_libro,fecha_d,estado))

    def limpiar_tabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)


    def mostrar_adv(self, error):
        messagebox.showwarning('Advertencia',error, parent = self.ventana)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo('Informacion', mensaje, parent=self.ventana)