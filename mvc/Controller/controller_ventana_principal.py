from View.app_view import VentanaPrincipal
from View.Panels.panel_book_view import PanelLibros
from View.Panels.panel_donacion_view import DonativoView

class Ventana:
    def __init__(self, controller_login, root, service_donativo, controller_admin):
        self.controller_admin = controller_admin
        self.ventana = root
        self.controller_login = controller_login
        self.service = service_donativo
        

        

    def cargar(self):
        self.GUI_ventana_principal._cargar_boton_administrativo()

    def mostrar_ventana(self):
        self.GUI_ventana_principal = VentanaPrincipal(self,self.ventana,PanelLibros,DonativoView,self.controller_admin)

    def donar_libro(self):

        panel = self.GUI_ventana_principal.panel_activo
        autor = panel.entry_nombre_autor.get()
        titulo = panel.entry_titulo.get()
        cantidad = panel.entry_cantidad.get()
        cedula_usuario = self.controller_login.cliente_recibido.identificador

        self.service.registrar_libro(autor,titulo,int(cantidad),cedula_usuario)

    def recibir_registros(self, panel):
        cedula_usuario = self.controller_login.cliente_recibido.identificador
        arreglo = self.service.buscar_registro(cedula_usuario)

        panel.insertar_tabla(arreglo)