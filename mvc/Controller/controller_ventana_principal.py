
from View.app_view import VentanaPrincipal
from View.Panels.panel_book_view import PanelLibros
from View.Panels.panel_donacion_view import DonativoView
from View.window_admin import InterfazAdmin


class Ventana:
    def __init__(self, controller, root):
        self.ventana = root
        self.controlador = controller
        self.controller_login = controller
        self.GUI_ventana_principal = VentanaPrincipal(controller, self.ventana, PanelLibros, DonativoView, InterfazAdmin)

    def cargar(self):
        self.GUI_ventana_principal._cargar_boton_administrativo()


    