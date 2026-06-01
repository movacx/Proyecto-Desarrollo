from View.Login.login_view import Login
from View.Login.register_view import Registro
from View.Login.recover_view import RecuperarPass

class LoginController:
    def __init__(self,root,service,ventanaPrincipal,service_donativo,controller_admin,service_libro, service_prestamo):
        self.cliente_recibido = None
        self.service = service
        self.service_libro = service_libro
        self.ventana = root
        self.ventana_principal = ventanaPrincipal
        self.service_donativo = service_donativo
        self.service_prestamo = service_prestamo
        self.controller_admin = controller_admin
        self.GUI_Login = Login(self, self.ventana)
    #-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==[ #Fin constructor ]--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#
    
    #Funciones encargadas de levantar las distintas interfaces: registro,recuperar contraseña y GUI principal.
    def btn_registrarse(self):
        self.GUI_Register = Registro(self, self.ventana)
    def btn_recuperar_contrasenna(self):
        self.GUI_recuperar = RecuperarPass(self, self.ventana)
    def btn_cargar_pantalla_principal(self):
        self.GUI_Login.contenedor.destroy()
        self.contenedor_principal = self.ventana_principal(self,self.ventana,self.service_donativo,self.controller_admin,self.service_libro,self.service_prestamo)
    #Fin

    #------------------------------------------ Registro del usuario ------------------------------------------
    def registrar_usuario(self):
        try:
            dni = self.GUI_Register.entry_dni.get()
            nombre = self.GUI_Register.entry_nombre.get()
            correo = self.GUI_Register.entry_correo.get()
            password = self.GUI_Register.entry_password.get()
            ped = self.GUI_Register.entry_ped.get()
            
            self.GUI_Register.mostrar_mensaje(self.service.registrar_cliente(dni,nombre,correo,password,ped))
            self.GUI_Register.limpiarCampos()
            self.GUI_Register.ventana.destroy()

        except Exception as error:
            self.GUI_Register.mostrar_adv(f'{error}')

    #------------------------------------------ Recuperacion del usuario --------------------------------------
    def recuperar_usuario(self):
        try:
            correo = self.GUI_recuperar.entry_correo.get()
            contra = self.GUI_recuperar.entry_password.get()
            ped_security = self.GUI_recuperar.entry_security_guard.get()

            mensaje = self.service.recuperar_cliente(correo, contra, ped_security)
            self.GUI_recuperar.mostrar_mensaje(mensaje)

        except Exception as error:
            self.GUI_recuperar.mostrar_adv(f'{error}')

    #------------------------------------------ Loggin del usuario ---------------------------------------------
    def acceder(self):
        try:
            correo = self.GUI_Login.entry_correo.get()
            contrasenna = self.GUI_Login.entry_password.get()
            self.cliente_recibido = self.service.loguearse(correo, contrasenna)

            if self.cliente_recibido.rol == 'Usuario':
                self.btn_cargar_pantalla_principal()
                self.contenedor_principal.mostrar_ventana()
                print('entrando como usuario', self.cliente_recibido)
                return self.cliente_recibido
            
            elif self.cliente_recibido.rol == 'Admin':
                print('Accediendo con el usuario administrativo:', self.cliente_recibido)
                self.GUI_Login.contenedor.destroy()
                self.contenedor_principal = self.ventana_principal(self,self.ventana,self.service_donativo,self.controller_admin,self.service_libro, self.service_prestamo)
                self.contenedor_principal.mostrar_ventana()
                self.contenedor_principal.cargar()

                return self.cliente_recibido
        except Exception as error:
            self.GUI_Login.mostrar_adv(f'{error}')

#-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==[ #Fin Clase ]--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#
        