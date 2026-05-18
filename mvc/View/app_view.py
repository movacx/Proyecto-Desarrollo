import tkinter as tk
from tkinter import ttk, messagebox


class VentanaPrincipal:
    def __init__(self, controller, root, panel_libro):
        self.manejo_controller = controller
        self.ventana = root
        self.ventana.geometry('1024x600')
        self.ventana.title('Principal - Biblioteca CoopePuntarenas')
        self.ventana.configure(bg='white')

        self._bar_menu()
        self._barra_laterial()
        self._parte_derecha()
        self._buttons()

        self.clase_libro = panel_libro
        self.panel_activo = None




    #work

    def _cambiar_panel(self):
        if self.panel_activo is not None:
            self.panel_activo.contenedor.destroy()

        self.panel_activo = self.clase_libro(self.campo_derecho)

#-=======================================================[PANEL DERECHO]============================================================================
    def _parte_derecha(self):
        self.campo_derecho = tk.Frame(self.ventana)
        self.campo_derecho.pack(side='right',fill='both', expand=True)

#-=======================================================[FIN DERECHO]============================================================================
#--Intocable--:
#-=======================================================[PANEL IZQUIERDO]============================================================================
    def _barra_laterial(self):
        self.barra_lateral = tk.Frame(self.ventana, bg="#6E7070")#,width = 400)
        self.barra_lateral.pack(side='left', fill='y')
        self.barra_lateral.pack_propagate(False)
        
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
                                         anchor = 'w',command = self._cambiar_panel)
        
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
        

    #----Fin intocable----



if __name__ == '__main__':
    root = tk.Tk()
    app = VentanaPrincipal(None, root, None)
    root.mainloop()
