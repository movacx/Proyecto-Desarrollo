import tkinter as tk
from tkinter import ttk, messagebox


class RecuperarPass:
    def __init__(self, controller, root):
        self.manejo_controller = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.title('Recover password - | Biblioteca CoopePuntarenas |')
        self._row_columns_configure()
        self.ventana.geometry('420x260')
        self.ventana.configure(bg="#6E7070")

        #Frame
        self.contenedor = tk.Frame(self.ventana, padx = 40, pady = 40)#, #bg="#29274C")
        self.contenedor.grid(row = 1, column=1)

        #settings
        self.ventana.configure(bg="black")
        self.contenedor.configure(bg='white')

        self._formulario()
        self._entry()
        self._buttons()

    def _formulario(self):
        tk.Label(self.contenedor, text = '| Recuperación de la cuenta |', font = ('Arial', 14, 'bold'),bg='white').grid(row=0,column = 0, columnspan = 2, pady = 10)
        tk.Label(self.contenedor, text = 'Correo:',bg='white').grid(row=1, column = 0, sticky = 'w', pady = 5)
        tk.Label(self.contenedor, text = 'Contraseña:',bg='white').grid(row=2, column = 0, sticky = 'w', pady = 5)
        tk.Label(self.contenedor, text = 'Animal Favorito?',bg='white').grid(row=3, column = 0, sticky = 'w', pady = 5)

    def _entry(self): #identificador, nombre, correo, passw, rol
        self.entry_correo = tk.Entry(self.contenedor, width = 40,bd=0,bg="#E3E3E3")
        self.entry_correo.grid(row = 1, column = 1, sticky = 'we',padx=(10,0))

        self.entry_password = tk.Entry(self.contenedor, show="#",bd=0,bg="#E3E3E3")
        self.entry_password.grid(row=2, column = 1, sticky = 'we',padx=(10,0))

        self.entry_security_guard = tk.Entry(self.contenedor,bd=0,bg="#E3E3E3")
        self.entry_security_guard.grid(row=3, column = 1, sticky = 'we',padx=(10,0))

    def _buttons(self):
        self.btn_aceptar = tk.Button(self.contenedor, text = 'Aceptar',command = lambda: self.manejo_controller.recuperar_usuario(),
                                     bd = 0,
                                     bg = '#DDE0E0',
                                     fg = 'black')
        self.btn_aceptar.grid(row = 4, column = 0, columnspan = 2, pady = 10)

    def limpiarCampos(self):
        self.entry_correo.delete(0,tk.END)
        self.entry_password.delete(0,tk.END)
        self.entry_security_guard.delete(0,tk.END)

    def _row_columns_configure(self):
        #raiz
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.rowconfigure(1, weight = 1)
        self.ventana.rowconfigure(2, weight = 1)

        self.ventana.columnconfigure(0, weight = 1)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.columnconfigure(2, weight = 1)

    def mostrar_adv(self, error):
        messagebox.showwarning('Advertencia',error, parent = self.ventana)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo('Informacion', mensaje, parent=self.ventana)

if __name__ == '__main__':
    root = tk.Tk()
    app = RecuperarPass(None, root)
    root.mainloop()
