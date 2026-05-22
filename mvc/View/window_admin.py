import tkinter as tk
from tkinter import ttk, messagebox


class InterfazAdmin:
    def __init__(self, controller, root):
        self.manejo_controller = controller
        self.ventana = root
        self.ventana.geometry('1024x600')
        self.ventana.title('Principal - Biblioteca CoopePuntarenas')
        self.ventana.configure(bg='white')

        self._barra_laterial()
        self._parte_derecha()
        self._buttons()


    def _cambiar_panel(self, tipo_panel):
        if self.panel_activo is not None:
            self.panel_activo.contenedor.destroy()        
        if tipo_panel is not None:
            self.panel_activo = tipo_panel(self.campo_derecho)
            
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
                                         anchor = 'w')
        
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

if __name__ == '__main__':
    root = tk.Tk()
    app = InterfazAdmin(None, root)
    root.mainloop()
    