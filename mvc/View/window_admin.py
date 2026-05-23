import tkinter as tk
from tkinter import ttk, messagebox

#archivo windows_Admin.py

class InterfazAdmin:
    def __init__(self, controller,root, panel_libro):
        self.ventana = tk.Toplevel(root)
        self.ventana.configure(bg='white')
        self.ventana.geometry('1024x600')
        self.controller = controller
        self.clase_registro_libro = panel_libro
        
        
        self.panel_activo = None

        self._parte_derecha()  
        self._barra_laterial() 
        self._buttons()      


# window_admin.py

    def _cambiar_panel(self, tipo_panel):
        if self.panel_activo is not None:
            self.panel_activo.contenedor.destroy()

        if tipo_panel is not None:
            self.panel_activo = tipo_panel(self.campo_derecho,self.controller
            )
            
#-=======================================================[PANEL DERECHO]============================================================================
    def _parte_derecha(self):
        self.campo_derecho = tk.Frame(self.ventana)
        self.campo_derecho.pack(side='right',fill='both', expand=True)

#-=======================================================[PANEL IZQUIERDO]============================================================================
    def _barra_laterial(self):
        self.barra_lateral = tk.Frame(self.ventana, bg="#6E7070")#,width = 400)
        self.barra_lateral.pack(side='left', fill='y')
        self.barra_lateral.pack_propagate(False)
        
                          #Lo deje asi para hacer mas ancho la barra ya que no pude con el width
        tk.Label(self.barra_lateral, text = '     Navegacion       ', font = ('Arial', 12, 'bold'),bg="#6E7070").grid(row=0,column=0, padx = 10, pady = 10)

    def _buttons(self):
        self.btn_ver_libros =  tk.Button(self.barra_lateral, text = '📚Registrar Libros',
                                         bg="#6E7070",
                                         fg = 'white',
                                         font = ('Arial', 11, 'bold'),
                                         bd=0,
                                         padx = 15,
                                         pady = 8,
                                         anchor = 'w',
                                         command = lambda: self._cambiar_panel(self.clase_registro_libro))
        
        self.btn_ver_libros.grid(row = 1, column = 0, pady = 5, sticky = 'we')
        #=-----------------------------------------------------------------------------------------
        self.btn_donar_libros = tk.Button(self.barra_lateral, text = '🫂Administrar donativos',
                                         bg="#6E7070",
                                         fg = 'white',
                                         font = ('Arial', 11, 'bold'),
                                         bd=0,
                                         padx = 15,
                                         pady = 8,
                                         anchor = 'w')
        self.btn_donar_libros.grid(row = 2, column = 0, pady = 5, sticky = 'we')
        #=-----------------------------------------------------------------------------------------
        self.btn_pedir_prestamo = tk.Button(self.barra_lateral, text = '🧾Administrar prestamos',
                                            bg = '#6E7070',
                                            fg='white',
                                            font = ('Arial', 11, 'bold'),
                                            padx = 5,
                                            pady = 5,
                                            anchor = 'w')
        self.btn_pedir_prestamo.grid(row=3, column = 0, pady = 5, sticky = 'we')
        #=-----------------------------------------------------------------------------------------

    def mostrar_adv(self, error):
        messagebox.showwarning('Advertencia',error, parent = self.ventana)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo('Informacion', mensaje, parent=self.ventana)