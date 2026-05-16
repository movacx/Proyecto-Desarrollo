import tkinter as tk

class Login:
    def __init__(self, controller, root):
        #Params
        self.manejo_controller = controller
        self.ventana = root
        self.ventana.geometry('700x900')
        self.ventana.title('Login - | Biblioteca CoopePuntarenas |')
        
        #settings
        self.ventana.configure(bg="#6E7070")

        #Frame
        self.contenedor = tk.Frame(self.ventana, padx = 40, pady = 40)#, #bg="#29274C")
        self.contenedor.grid(row = 1, column=1)

        #Llamados
        self._row_columns_configure()
        self._labels()   
        self._entry()
        self._buttons()

                    #=-=-=-=-=-=-=-=-=Fin del constructor=-=-=-=-=-=-=-=-=


    def _labels(self):
        tk.Label(self.contenedor, text = '| Biblioteca CoopePuntarenas |', font = ('Arial', 12, 'bold')).grid(row=0,column=0, 
                                                                                                              columnspan=2, 
                                                                                                              pady=(0,20),
                                                                                                              sticky='nswe')
        #______________________________________________________________________________________________________________________
        tk.Label(self.contenedor, text = 'Correo:').grid(row=1, column = 0, sticky = 'w', pady = 5)
        tk.Label(self.contenedor, text = 'Contraseña:').grid(row=2, column = 0, sticky = 'w', pady = 5)

    #-==--=-=-==--=-=-=-=-=-=-=-=-==--=-=-=-=-==--=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-==--==--=-=-=-==--=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-==--=-==-
    def _entry(self): #identificador, nombre, correo, passw, rol
        self.entry_correo = tk.Entry(self.contenedor, width = 40)
        self.entry_correo.grid(row = 1, column = 1, sticky = 'we',padx=(10,0))

        self.entry_password = tk.Entry(self.contenedor, show="#")
        self.entry_password.grid(row=2, column = 1, sticky = 'we',padx=(10,0))

    #-==--=-=-==--=-=-=-=-=-=-=-=-==--=-=-=-=-==--=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-==--==--=-=-=-==--=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-==--=-==-
    def _buttons(self):
        self.btn_acceder = tk.Button(self.contenedor, text = 'Ingresar', command = lambda: self.manejo_controller.btn_cargar_pantalla_principal())
        self.btn_acceder.grid(row = 3, column = 1, sticky = 'we', pady = 10)

        self.btn_registrarse = tk.Button(self.contenedor, text = 'Registro', command = lambda: self.manejo_controller.btn_registrarse())
        self.btn_registrarse.grid(row=3, column = 0, sticky = 'w', pady = 10)

        self.btn_recuperar_pass = tk.Button(self.contenedor, text = 'Olvide mi contraseña', command = lambda: self.manejo_controller.btn_recuperar_contrasenna())
        self.btn_recuperar_pass.grid(row=4, column = 0, sticky = 'nswe',columnspan=3)

    #-==--=-=-==--=-=-=-=-=-=-=-=-==--=-=-=-=-==--=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-==--==--=-=-=-==--=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-==--=-==-
    


    
    def _row_columns_configure(self):
        #raiz
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.rowconfigure(1, weight = 1)
        self.ventana.rowconfigure(2, weight = 1)

        self.ventana.columnconfigure(0, weight = 1)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.columnconfigure(2, weight = 1)
        

#Testeo de Interfaz
if __name__ == '__main__':

    root = tk.Tk()
    app = Login(None, root)
    root.mainloop()
