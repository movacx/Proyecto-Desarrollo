from View.login_view import Login
from View.register_view import Registro
from View.recover_view import RecuperarPass

from View.app_view import VentanaPrincipal

class LoginController:
    def __init__(self, root, service):
        self.service = service
        self.ventana = root
        self.GUI_Login = Login(self, self.ventana)

        #Fin constructor

    #=--=-==-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    def btn_registrarse(self):
        self.GUI_Register = Registro(self, self.ventana)
    def btn_recuperar_contrasenna(self):
        self.GUI_recuperar = RecuperarPass(self, self.ventana)
    def btn_cargar_pantalla_principal(self):
        self.GUI_Login.contenedor.destroy()
        self.GUI_ventana_principal = VentanaPrincipal(self, self.ventana)
    #=--=-==-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

    #Forms
    def registrar_usuario(self):
        try:
            dni = self.GUI_Register.entry_dni.get()
            nombre = self.GUI_Register.entry_nombre.get()
            correo = self.GUI_Register.entry_correo.get()
            password = self.GUI_Register.entry_password.get()
            ped = self.GUI_Register.entry_ped.get()

            self.service.registrar_cliente(dni,nombre,correo,password,ped)
            self.GUI_Register.mostrar_mensaje('Exito al registrar!')
            self.GUI_Register.limpiarCampos()
            self.GUI_Register.ventana.destroy()

        except Exception as error:
            self.GUI_Register.mostrar_adv(f'{error}')

    def recuperar_usuario(self):
        # try:
        correo = self.GUI_recuperar.entry_correo.get()
        contra = self.GUI_recuperar.entry_password.get()
        ped_security = self.GUI_recuperar.entry_security_guard.get()

        mensaje = self.service.recuperar_cliente(correo, contra, ped_security)
        self.GUI_recuperar.mostrar_mensaje(mensaje)

        # except Exception as error:
        #     self.GUI_recuperar.mostrar_adv(f'{error}')





        