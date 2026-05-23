from View.Panels.admin_registro_libro import RegistroLibro
from View.window_admin import InterfazAdmin

from Service.libro_service import LibroService
from Repository.repositorio import Repository

#archivo controller_ventana_Adm.py
class VentanaAdministrativa:
    def __init__(self, root):
        self.ventana = root
        self.service = LibroService(Repository)
        self.GUI_ventana_principal = InterfazAdmin(self,self.ventana,RegistroLibro)

    def agregar_libro(self):
        panel = self.GUI_ventana_principal.panel_activo

        titulo = panel.entry_titulo.get()
        autor = panel.entry_autor.get()
        inventario = panel.entry_inventario.get()
        categoria = panel.entry_categoria.get()
        
        self.service.registrar_libro(titulo,autor,int(inventario),categoria)
        self.GUI_ventana_principal.mostrar_mensaje('Registrado con exito!')



        
