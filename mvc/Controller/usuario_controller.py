from View.ventana_usuario import VentanaPrincipal
from View.Frame.user_busq_libro_frame import PanelLibros
from View.Frame.user_donaciones_frame import DonativoView
from View.Frame.user_prestamo_frame import PrestamoUsuario
from View.Frame.user_gestionprestamo_frame import DevolverPrestamo

class ControladorVentanaPrincipal:
    def __init__(self, controller_login, root, service_donativo, controller_admin,service_libro, service_prestamo):
        self.controller_admin = controller_admin
        self.ventana = root
        self.controller_login = controller_login
        self.service_donativo = service_donativo
        self.service_libro = service_libro
        self.service_prestamo = service_prestamo
        
    #-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==[ #Fin constructor ]--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#

    #Funcion encargada de cargar el panel administrativo si el usuario cuenta con los permisos necesarios.
    def cargar(self):
        self.GUI_ventana_principal._cargar_boton_administrativo()

    #Cargar esta ventana (aplica despues de pasar del login)
    def mostrar_ventana(self):
        self.GUI_ventana_principal = VentanaPrincipal(self,self.ventana,PanelLibros,DonativoView, PrestamoUsuario, DevolverPrestamo, self.controller_admin)

    #-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#

    #Funciones del Frame (donaciones)
    def donar_libro(self):
        try:
            panel = self.GUI_ventana_principal.panel_activo
            autor = panel.entry_nombre_autor.get()
            titulo = panel.entry_titulo.get()
            cantidad = panel.entry_cantidad.get()
            cedula_usuario = self.controller_login.cliente_recibido.identificador
            self.GUI_ventana_principal.mostrar_mensaje(self.service_donativo.crear_donacion(autor,titulo,int(cantidad),cedula_usuario))
            panel.limpiar_tabla()
            panel.limpiar_campos()
            panel.cargar()
            
        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)

    def recibir_registros(self, panel):
        try:
            cedula_usuario = self.controller_login.cliente_recibido.identificador
            arreglo = self.service_donativo.buscar_registro(cedula_usuario)
            panel.insertar_tabla(arreglo)
        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)

    #-----------------------------------------------------------------------------------------------------#
    #Funciones del Frame (Libro)
    def cargar_filtrado_categoria(self, panel):
        panel.limpiar_tabla()
        opcion_seleccionada = panel.combobox.get()
        
        coincidencias_encontradas = self.service_libro.filtrar_categoria(opcion_seleccionada)

        panel.insertar_tabla(coincidencias_encontradas)

    def cargar_filtrado_nombre(self, panel): 
        panel.limpiar_tabla()
        nombre_libro = panel.entry_barra_busqueda.get()
        coincidencias_encontradas = self.service_libro.buscar_libro(nombre_libro)
        panel.insertar_tabla(coincidencias_encontradas)

    #-----------------------------------------------------------------------------------------------------#
    #Funciones del Frame (prestamo)
    def registrar_prestamo(self, panel):
        dni = panel.entrada_dni.get()
        id_lib = panel.id_libro.get()
        panel.mostrar_mensaje(self.service_prestamo.registrar_prestamo(id_lib,dni))


    def listar_prestamos(self, panel):
        dni_precargado = panel.entrada_dni.get()
        
        prestamos_encontrados = self.service_prestamo.mostrar_prestamos_cliente(dni_precargado)
        
        panel.insertar_tabla(prestamos_encontrados)

    ##### Adicional: Frame ((DevolverPrestamo)) ######
    def accion_devolver_libro(self, panel):
        id_prestamo = panel.id_prestamo.get()
        panel.mostrar_mensaje(self.service_prestamo.devolver_libro(id_prestamo))
        
        panel.cargar()
            



