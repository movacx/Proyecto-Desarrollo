from View.Frame.admin_libro_frame import RegistroLibro
from View.Frame.admin_donaciones_frame import AdministradorLibros
from View.ventana_administrativa import InterfazAdmin

class ControladorVentanaAdministrativa:
    def __init__(self, root, service_libro, service_donativo):
        self.ventana = root
        self.service_libro = service_libro
        self.service_donativo = service_donativo
        
    #-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==[ #Fin constructor ]--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#
    #Carga esta ventana (aplica despues de pulsar el boton dinamico)
    def mostrar_ventana(self):
        self.GUI_ventana_principal = InterfazAdmin(self,self.ventana,RegistroLibro,AdministradorLibros)

    #-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#

    #Funciones del Frame_Admin (donaciones)
    def recibir_registros(self, panel):
        try:
            arreglo = self.service_donativo.listar_registros()
            panel.insertar_tabla(arreglo,0)
        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)

    def cargar_filtrado_cliente(self):
        try:
            panel = self.GUI_ventana_principal.panel_activo
            ide = panel.entry_cliente.get()
            arreglo = self.service_donativo.buscar_registro(ide)
            panel.insertar_tabla(arreglo,1) 
        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)

    #-----------------------------------------------------------------------------------------------------#
    #Funciones del Frame_Admin (Libro)
    def agregar_libro(self):
        try:
            self.panel = self.GUI_ventana_principal.panel_activo
            titulo = self.panel.entry_titulo.get()
            autor = self.panel.entry_autor.get()
            inventario = self.panel.entry_inventario.get()
            categoria = self.panel.entry_categoria.get()
        
            self.service_libro.registrar_libro(titulo,autor,int(inventario),categoria)
            self.GUI_ventana_principal.mostrar_mensaje('Registrado con exito!')
            self.panel.cargar()
        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)

    #Adicional: Encargada de trepar el registro de la donacion al JSON de Libro, 
    #[Aplica despues de que haya sido aprobada] - USA EL SERVICE LIBRO
    def registrar_donacion(self):
        try:
            self.panel = self.GUI_ventana_principal.panel_activo
            ide = self.panel.entry_id.get()
            categoria = self.panel.lista_opciones.get()
            self.service_libro.administrar_donacion(ide, categoria)
        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)
    #-----------------------------------------------------------------------------------------------------#



    


        
