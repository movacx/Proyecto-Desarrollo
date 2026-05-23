import tkinter as tk

#archivo admin_registro_libro

class RegistroLibro:
    def __init__(self, enlace_ventana, controller):
        self.manejo_controller = controller
        self.contenedor = tk.Frame(enlace_ventana)
        self.contenedor.pack(side='right',fill='both',expand=True)
        self.contenedor.columnconfigure(0, weight=0)
        self.contenedor.columnconfigure(1, weight=1)
        self.contenedor.columnconfigure(2, weight=0)
        self._forms()
        self._buttons()

    def _forms(self):
        tk.Label(self.contenedor, text = 'Registro de libro', font = ('Arial', 11, 'bold')).grid(row=0,column=0,columnspan=3)

        tk.Label(self.contenedor, text = 'Autor:' ).grid(row=1,column=0,sticky='w')
        self.entry_autor = tk.Entry(self.contenedor)
        self.entry_autor.grid(row=1,column=1,sticky='we')

        tk.Label(self.contenedor, text = 'Titulo:' ).grid(row=2,column=0,sticky='w')
        self.entry_titulo = tk.Entry(self.contenedor)
        self.entry_titulo.grid(row=2,column=1,sticky='we')

        tk.Label(self.contenedor, text = 'Inventario:' ).grid(row=3,column=0,sticky='w')
        self.entry_inventario = tk.Entry(self.contenedor)
        self.entry_inventario.grid(row=3,column=1,sticky='we')

        tk.Label(self.contenedor, text = 'Categoria:').grid(row=5,column=0,sticky='w')
        self.entry_categoria = tk.Entry(self.contenedor)
        self.entry_categoria.grid(row=5,column=1,sticky='we')

    def _buttons(self):
        self.btn_aceptar =  tk.Button(self.contenedor, text = 'Registrar Libro',
                                         bg="#6E7070",
                                         fg = 'white',
                                         font = ('Arial', 11, 'bold'),
                                         bd=0,
                                         padx = 15,
                                         pady = 8,
                                         anchor = 'w',
                                         command = lambda: self.manejo_controller.agregar_libro())
        
        self.btn_aceptar.grid(row = 6, column = 0, pady = 10, columnspan=3)

