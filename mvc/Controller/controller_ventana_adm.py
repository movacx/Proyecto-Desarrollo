from View.Panels.admin_registro_libro import RegistroLibro
from View.Panels.admin_donaciones import AdministradorLibros
from View.window_admin import InterfazAdmin

#archivo controller_ventana_Adm.py
class VentanaAdministrativa:
    def __init__(self, root, service_libro, service_donativo):
        self.ventana = root
        self.service = service_libro
        self.service_donativo = service_donativo
        
        
    def mostrar_ventana(self):
        self.GUI_ventana_principal = InterfazAdmin(self,self.ventana,RegistroLibro,AdministradorLibros)

    def agregar_libro(self):
        self.panel = self.GUI_ventana_principal.panel_activo
        titulo = self.panel.entry_titulo.get()
        autor = self.panel.entry_autor.get()
        inventario = self.panel.entry_inventario.get()
        categoria = self.panel.entry_categoria.get()
    
        self.service.registrar_libro(titulo,autor,int(inventario),categoria)
        self.GUI_ventana_principal.mostrar_mensaje('Registrado con exito!')

    def recibir_registros(self, panel):
        arreglo = self.service_donativo.listar_registros()

        panel.insertar_tabla(arreglo,0)

    def registrar_donacion(self):
        self.panel = self.GUI_ventana_principal.panel_activo
        
        ide = self.panel.entry_id.get()
        categoria = self.panel.lista_opciones.get()

        self.service.administrar_donacion(ide, categoria)

    def cargar_filtrado_cliente(self):
        panel = self.GUI_ventana_principal.panel_activo
        ide = panel.entry_cliente.get()
        arreglo = self.service_donativo.buscar_registro(ide)
        panel.insertar_tabla(arreglo,1)





    


        
