
from View.app_view import VentanaPrincipal
from View.Panels.panel_book_view import PanelLibros
from View.Panels.panel_donacion_view import DonativoView
#archivo controller_ventana_principal.py
from Controller.controller_ventana_adm import VentanaAdministrativa

class Ventana:
    def __init__(self, controller, root):
        self.ventana = root
        self.controller_login = controller
        self.GUI_ventana_principal = VentanaPrincipal(controller, self.ventana, PanelLibros, DonativoView, VentanaAdministrativa)

    def cargar(self):
        self.GUI_ventana_principal._cargar_boton_administrativo()

        


    