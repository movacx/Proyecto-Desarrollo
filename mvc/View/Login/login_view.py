import tkinter as tk
from tkinter import messagebox, ttk

#archivo login_view.py

class Login:
    def __init__(self, controller, root):
        #Params
        self.manejo_controller = controller
        self.ventana = root
        self.ventana.geometry('600x500')
        self.ventana.title('Login - | Biblioteca CoopePuntarenas |')
        

        #Frame
        self.contenedor = tk.Frame(self.ventana, padx = 40, pady = 40)#, #bg="#29274C")
        self.contenedor.grid(row = 1, column=1)
        
        #settings
        self.ventana.configure(bg="black")
        self.contenedor.configure(bg='white')

        #Llamados
        self._row_columns_configure()
        self._labels()   
        self._entry()
        self._buttons()

                    #=-=-=-=-=-=-=-=-=Fin del constructor=-=-=-=-=-=-=-=-=


    def _labels(self):
        tk.Label(self.contenedor, text = '| Biblioteca CoopePuntarenas |', font = ('Arial', 12, 'bold'),bg='white').grid(row=0,column=0, 
                                                                                                              columnspan=2, 
                                                                                                              pady=(0,20),
                                                                                                              sticky='nswe')
        #______________________________________________________________________________________________________________________
        tk.Label(self.contenedor, text = 'Correo:',bg='white').grid(row=1, column = 0, sticky = 'w', pady = 5)
        tk.Label(self.contenedor, text = 'Contraseña:',bg='white').grid(row=2, column = 0, sticky = 'w', pady = 5)

    #-==--=-=-==--=-=-=-=-=-=-=-=-==--=-=-=-=-==--=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-==--==--=-=-=-==--=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-==--=-==-
    def _entry(self): #identificador, nombre, correo, passw, rol
        self.entry_correo = tk.Entry(self.contenedor, width = 40,bd=0,bg="#E3E3E3")
        self.entry_correo.grid(row = 1, column = 1, sticky = 'we',padx=(10,0))

        self.entry_password = tk.Entry(self.contenedor, show="#",bd=0,bg="#E3E3E3")
        self.entry_password.grid(row=2, column = 1, sticky = 'we',padx=(10,0))

    #-==--=-=-==--=-=-=-=-=-=-=-=-==--=-=-=-=-==--=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-==--==--=-=-=-==--=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-==--=-==-
    def _buttons(self):
        self.btn_acceder = tk.Button(self.contenedor, text = 'Ingresar', command = lambda: self.manejo_controller.acceder(),
                                     bd = 0,
                                     bg = '#DDE0E0',
                                     fg = 'black')
        self.btn_acceder.grid(row = 3, column = 1, sticky = 'we', pady = 10)

        self.btn_registrarse = tk.Button(self.contenedor, text =   '   Registro   ', command = lambda: self.manejo_controller.btn_registrarse(),
                                         bd = 0,
                                         bg = "#DDE0E0",
                                         fg = 'black')
        self.btn_registrarse.grid(row=3, column = 0, sticky = 'w', pady = 10)

        self.btn_recuperar_pass = tk.Button(self.contenedor, text = 'Recuperar Contraseña', command = lambda: self.manejo_controller.btn_recuperar_contrasenna(),
                                             bd = 0,
                                             bg = "#DDE0E0",
                                             fg = 'black')
        self.btn_recuperar_pass.grid(row=4, column = 0, sticky = 'nswe',columnspan=3)

    #-==--=-=-==--=-=-=-=-=-=-=-=-==--=-=-=-=-==--=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-==--==--=-=-=-==--=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-==--=-==-
    
    def mostrar_adv(self, error):
        messagebox.showwarning('Advertencia',error, parent = self.ventana)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo('Informacion', mensaje, parent=self.ventana)


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
#Testeo de Interfaz
if __name__ == '__main__':

    root = tk.Tk()
    app = Login(None, root)
    root.mainloop()
