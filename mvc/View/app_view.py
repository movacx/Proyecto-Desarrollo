import tkinter as tk

class VentanaPrincipal:
    def __init__(self, controller, root):
        self.manejo_controller = controller
        self.ventana = root
        self.ventana.geometry('1024x600')
        self.ventana.title('Principal - Biblioteca CoopePuntarenas')
        self.ventana.configure(bg='white')
        self._bar_menu()
        self._barra_laterial()
        self._buttons()


    def _barra_laterial(self):
        self.barra_lateral = tk.Frame(self.ventana, bg="#6E7070")#,width = 400)
        self.barra_lateral.pack(side='left', fill='y')
        self.barra_lateral.pack_propagate(False)


    def _parte_derecha(self):
        self.campo_derecho = tk.Frame(self.ventana)
        self.campo_derecho.pack(side='right',fill='x')
        
                          #Lo deje asi para hacer mas ancho la barra ya que no pude con el width
        tk.Label(self.barra_lateral, text = '     Navegacion       ', font = ('Arial', 12, 'bold'),bg="#6E7070").grid(row=0,column=0, padx = 10, pady = 10)

    def _buttons(self):
        self.btn_ver_libros =  tk.Button(self.barra_lateral, text = '📚Ver libros',
                                         bg="#6E7070",
                                         fg = 'white',
                                         font = ('Arial', 11, 'bold'),
                                         bd=0,
                                         padx = 15,
                                         pady = 8,
                                         anchor = 'w')
        
        self.btn_ver_libros.grid(row = 1, column = 0, pady = 5, sticky = 'we')
        #=-----------------------------------------------------------------------------------------
        self.btn_donar_libros = tk.Button(self.barra_lateral, text = '🫂Donar Libros',
                                         bg="#6E7070",
                                         fg = 'white',
                                         font = ('Arial', 11, 'bold'),
                                         bd=0,
                                         padx = 15,
                                         pady = 8,
                                         anchor = 'w')
        self.btn_donar_libros.grid(row = 2, column = 0, pady = 5, sticky = 'we')
        #=-----------------------------------------------------------------------------------------
        self.btn_pedir_prestamo = tk.Button(self.barra_lateral, text = '🧾Solicitar Prestamo',
                                            bg = '#6E7070',
                                            fg='white',
                                            font = ('Arial', 11, 'bold'),
                                            padx = 5,
                                            pady = 5,
                                            anchor = 'w')
        self.btn_pedir_prestamo.grid(row=3, column = 0, pady = 5, sticky = 'we')
        #=-----------------------------------------------------------------------------------------


    def _bar_menu(self):
        menu = tk.Menu(self.ventana, bg="#A9A9A9")
        self.ventana.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label='Usuario', menu = file_menu)
        file_menu.add_command(label='Configuracion')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command = self.ventana.quit)

        help_menu = tk.Menu(menu)
        menu.add_cascade(label='Help', menu = help_menu)
        help_menu.add_command(label='Bienvenida')
        help_menu.add_command(label='Informacion')
        help_menu.add_separator()
        





if __name__ == '__main__':
    root = tk.Tk()
    app = VentanaPrincipal(None, root)
    root.mainloop()
