from View.Panels.admin_registro_libro import RegistroLibro
from View.window_admin import InterfazAdmin

#archivo controller_ventana_Adm.py
class VentanaAdministrativa:
    def __init__(self, root, service_libro):
        self.ventana = root
        self.service = service_libro
        
        
    def mostrar_ventana(self):
        self.GUI_ventana_principal = InterfazAdmin(self,self.ventana,RegistroLibro)

    def agregar_libro(self):
        self.panel = self.GUI_ventana_principal.panel_activo
        titulo = self.panel.entry_titulo.get()
        autor = self.panel.entry_autor.get()
        inventario = self.panel.entry_inventario.get()
        categoria = self.panel.entry_categoria.get()
    
        self.service.registrar_libro(titulo,autor,int(inventario),categoria)
        self.GUI_ventana_principal.mostrar_mensaje('Registrado con exito!')



        
