import tkinter as tk
from tkinter import ttk, messagebox

#archivo app_view.py
class VentanaPrincipal:
    def __init__(self, controller, root, panel_libro, panel_donacion, panel_prestamo, panel_devolver_prestamo, panel_administrativo):
        self.manejo_controller = controller
        self.ventana = root
        self.ventana.geometry('1366x768')
        self.ventana.title('Principal - Biblioteca CoopePuntarenas')
        self.ventana.configure(bg='white')

        self.clase_libro = panel_libro
        self.clase_donativo = panel_donacion
        self.panel_activo = None
        self.clase_administrativa = panel_administrativo
        self.clase_prestamo = panel_prestamo
        self.clase_devolver_prestamo = panel_devolver_prestamo

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
        self.barra_lateral = tk.Frame(self.ventana, bg="#000000")
        self.barra_lateral.pack(side='left', fill='y')
        self.barra_lateral.pack_propagate(False)
        tk.Label(self.barra_lateral, text = '     Navegacion       ', font = ('Arial', 11, 'bold underline'),bg="#000000",fg='white').grid(row=0,column=0, padx = 10, pady = 10)

    def _buttons(self):
        #boton ver_libros
        self.btn_ver_libros =  tk.Button(self.barra_lateral, text = '📚Ver libros',
                                         bg="#000000",
                                         fg = 'white',
                                         font = ('Arial', 11, 'bold'),
                                         bd=0,
                                         padx = 15,
                                         pady = 8,
                                         anchor = 'w',command=lambda :  self._cambiar_panel(self.clase_libro))

        self.btn_ver_libros.grid(row = 1, column = 0, pady = 5, sticky = 'we')

        #boton donar_libros
        self.btn_donar_libros = tk.Button(self.barra_lateral, text = '🫂Donar Libros',
                                         bg="#000000",
                                         fg = 'white',
                                         font = ('Arial', 11, 'bold'),
                                         bd=0,
                                         padx = 15,
                                         pady = 8,
                                         anchor = 'w', command = lambda:self._cambiar_panel(self.clase_donativo))
        self.btn_donar_libros.grid(row = 2, column = 0, pady = 5, sticky = 'we')

        #boton pedir_prestamo
        self.btn_pedir_prestamo = tk.Button(self.barra_lateral, text = '🧾Solicitar Prestamo',
                                            bg = "#000000",
                                            fg='white',
                                            font = ('Arial', 11, 'bold'),
                                            bd=0,
                                            padx = 5,
                                            pady = 5,
                                            anchor = 'w',
                                            command=lambda : self._cambiar_panel(self.clase_prestamo))
        self.btn_pedir_prestamo.grid(row=3, column = 0, pady = 5, sticky = 'we')

        self.btn_devolver_prestamo = tk.Button(self.barra_lateral, text = '🗃️Administrar mis prestamos',
                                            bg = "#000000",
                                            fg='white',
                                            font = ('Arial', 11, 'bold'),
                                            bd=0,
                                            padx = 5,
                                            pady = 5,
                                            anchor = 'w',
                                            command=lambda : self._cambiar_panel(self.clase_devolver_prestamo))
        self.btn_devolver_prestamo.grid(row=4, column = 0, pady = 5, sticky = 'we')




    def _cargar_boton_administrativo(self):
        self.btn_administrativo = tk.Button(self.barra_lateral, text = '📇Panel Administrativo',
                                            bg = "#FFFFFF",
                                            fg='black',
                                            font = ('Arial', 11, 'bold'),
                                            bd = 0,
                                            padx = 5,
                                            pady = 5,
                                            anchor = 'w',
                                            command = lambda: self.clase_administrativa.mostrar_ventana())
        self.btn_administrativo.grid(row=5, column=0, pady=370, sticky='we')

    #-=======================================================[FIN IZQUIERDO]============================================================================

    def _bar_menu(self):
        menu = tk.Menu(self.ventana, bg="#A9A9A9")
        self.ventana.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Usuario', menu=file_menu)
        file_menu.add_command(
            label='Configuracion',
            command=lambda: self.clase_administrativa.mostrar_ventana()
        )
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.ventana.quit)

        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='Bienvenida', command=self.mostrar_bienvenida)
        help_menu.add_command(label='Informacion', command=self.mostrar_informacion)
        help_menu.add_separator()

    def mostrar_bienvenida(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Bienvenida")
        ventana.geometry("500x300")
        ventana.configure(bg="#111111")
        ventana.resizable(False, False)

        tk.Label(
            ventana,
            text="📚 Biblioteca CoopePuntarenas",
            font=("Arial", 18, "bold"),
            bg="#111111",
            fg="white"
        ).pack(pady=20)

        tk.Label(
            ventana,
            text="Bienvenido al sistema de biblioteca.\n\n"
                 "Aquí puedes consultar libros, donar libros,\n"
                 "solicitar préstamos y administrar tus préstamos.",
            font=("Arial", 12),
            bg="#111111",
            fg="#DDDDDD",
            justify="center"
        ).pack(pady=10)

        tk.Button(
            ventana,
            text="Cerrar",
            font=("Arial", 11, "bold"),
            bg="#2E8B57",
            fg="white",
            width=15,
            command=ventana.destroy
        ).pack(pady=25)

    def mostrar_informacion(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Información")
        ventana.geometry("500x320")
        ventana.configure(bg="#111111")
        ventana.resizable(False, False)

        tk.Label(
            ventana,
            text="ℹ️ Información del Sistema",
            font=("Arial", 18, "bold"),
            bg="#111111",
            fg="white"
        ).pack(pady=20)

        tk.Label(
            ventana,
            text="Sistema: Biblioteca CoopePuntarenas\n"
                 "Versión: 1.0\n"
                 "Lenguaje: Python\n"
                 "Interfaz: Tkinter\n\n"
                 "Este sistema permite gestionar libros,\n"
                 "donaciones, préstamos y usuarios.",
            font=("Arial", 12),
            bg="#111111",
            fg="#DDDDDD",
            justify="center"
        ).pack(pady=10)

        tk.Button(
            ventana,
            text="Cerrar",
            font=("Arial", 11, "bold"),
            bg="#4169E1",
            fg="white",
            width=15,
            command=ventana.destroy
        ).pack(pady=25)


    def mostrar_adv(self, error):
        messagebox.showwarning('Advertencia',error, parent = self.ventana)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo('Informacion', mensaje, parent=self.ventana)

if __name__ == '__main__':
    root = tk.Tk()
    ventana = tk.Frame(root).pack()
    app = VentanaPrincipal(None, root,ventana )
    root.mainloop()
