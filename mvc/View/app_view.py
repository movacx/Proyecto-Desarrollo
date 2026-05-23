import tkinter as tk
from tkinter import ttk, messagebox

#archivo app_view.py
class VentanaPrincipal:
    def __init__(self, controller, root, panel_libro, panel_donacion, panel_administrativo, ):
        self.manejo_controller = controller
        self.ventana = root
        self.ventana.geometry('1366x768')
        self.ventana.title('Principal - Biblioteca CoopePuntarenas')
        self.ventana.configure(bg='white')

        self.clase_libro = panel_libro
        self.clase_donativo = panel_donacion
        self.panel_activo = None
        self.clase_administrativa = panel_administrativo

        self._bar_menu()
        self._parte_derecha()  
        self._barra_laterial()
        self._buttons()       


    def _cambiar_panel(self, tipo_panel):
        if self.panel_activo is not None:
            self.panel_activo.contenedor.destroy()        
        if tipo_panel is not None:
            self.panel_activo = tipo_panel(self.campo_derecho,self.manejo_controller)
            


#-=======================================================[PANEL DERECHO]============================================================================
    def _parte_derecha(self):
        self.campo_derecho = tk.Frame(self.ventana)
        self.campo_derecho.pack(side='right',fill='both', expand=True)





#-=======================================================[PANEL IZQUIERDO]============================================================================
    def _barra_laterial(self):
        self.barra_lateral = tk.Frame(self.ventana, bg="#6E7070")
        self.barra_lateral.pack(side='left', fill='y')
        self.barra_lateral.pack_propagate(False)
        tk.Label(self.barra_lateral, text = '     Navegacion       ', font = ('Arial', 12, 'bold'),bg="#6E7070").grid(row=0,column=0, padx = 10, pady = 10)

    def _buttons(self):
        #boton ver_libros
        self.btn_ver_libros =  tk.Button(self.barra_lateral, text = '📚Ver libros',
                                         bg="#6E7070",
                                         fg = 'white',
                                         font = ('Arial', 11, 'bold'),
                                         bd=0,
                                         padx = 15,
                                         pady = 8,
                                         anchor = 'w',command=lambda :  self._cambiar_panel(self.clase_libro))
        
        self.btn_ver_libros.grid(row = 1, column = 0, pady = 5, sticky = 'we')

        #boton donar_libros
        self.btn_donar_libros = tk.Button(self.barra_lateral, text = '🫂Donar Libros',
                                         bg="#6E7070",
                                         fg = 'white',
                                         font = ('Arial', 11, 'bold'),
                                         bd=0,
                                         padx = 15,
                                         pady = 8,
                                         anchor = 'w', command = lambda:self._cambiar_panel(self.clase_donativo))
        self.btn_donar_libros.grid(row = 2, column = 0, pady = 5, sticky = 'we')

        #boton pedir_prestamo
        self.btn_pedir_prestamo = tk.Button(self.barra_lateral, text = '🧾Solicitar Prestamo',
                                            bg = '#6E7070',
                                            fg='white',
                                            font = ('Arial', 11, 'bold'),
                                            padx = 5,
                                            pady = 5,
                                            anchor = 'w')
        self.btn_pedir_prestamo.grid(row=3, column = 0, pady = 5, sticky = 'we')


    def _cargar_boton_administrativo(self):
        self.btn_administrativo = tk.Button(self.barra_lateral, text = '📇Panel Administrativo',
                                            bg = '#6E7070',
                                            fg='white',
                                            font = ('Arial', 11, 'bold'),
                                            padx = 5,
                                            pady = 5,
                                            anchor = 'w',
                                            command = lambda: self.clase_administrativa.mostrar_ventana())
        self.btn_administrativo.grid(row=4, column=0, pady=370, sticky='we')

    #-=======================================================[FIN IZQUIERDO]============================================================================

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
    ventana = tk.Frame(root).pack()
    app = VentanaPrincipal(None, root,ventana )
    root.mainloop()
