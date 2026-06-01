from View.Frame.admin_libro_frame import RegistroLibro
from View.Frame.admin_donaciones_frame import AdministradorLibros
from View.Frame.admin_reportes_frame import ReportesAdmin
from View.ventana_administrativa import InterfazAdmin
from Service.reporte_service import ReporteService


class ControladorVentanaAdministrativa:
    def __init__(self, root, service_libro, service_donativo, service_prestamo):
        self.ventana = root

        self.service_libro = service_libro
        self.service_donativo = service_donativo
        self.service_prestamo = service_prestamo

        self.reporte_service = ReporteService(
            self.service_libro,
            self.service_donativo,
            self.service_prestamo
        )

    def mostrar_ventana(self):
        self.GUI_ventana_principal = InterfazAdmin(
            self,
            self.ventana,
            RegistroLibro,
            AdministradorLibros,
            ReportesAdmin
        )

    # ===================== REPORTES =====================

    def generar_reporte_general(self):
        return self.reporte_service.generar_reporte_general()

    def listar_libros(self):
        if hasattr(self.service_libro, "listar_libros"):
            return self.service_libro.listar_libros()
        return self.service_libro.repo.listar()

    def listar_donativos(self):
        if hasattr(self.service_donativo, "listar_donaciones"):
            return self.service_donativo.listar_donaciones()
        if hasattr(self.service_donativo, "listar_registros"):
            return self.service_donativo.listar_registros()
        return self.service_donativo.repo.listar()

    def listar_prestamos(self):
        if hasattr(self.service_prestamo, "listar_prestamos"):
            return self.service_prestamo.listar_prestamos()
        return self.service_prestamo.repo.listar()

    # ===================== DONACIONES =====================

    def recibir_registros(self, panel):
        try:
            arreglo = self.service_donativo.listar_registros()
            panel.insertar_tabla(arreglo, 0)
        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)

    def cargar_filtrado_cliente(self):
        try:
            panel = self.GUI_ventana_principal.panel_activo

            panel.limpiar_tabla()
            panel.bloquear_botones()

            ide = panel.entry_cliente.get()

            arreglo = self.service_donativo.buscar_registro(ide)

            panel.insertar_tabla(arreglo, 1)

        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)

    def registrar_donacion(self):
        try:
            panel = self.GUI_ventana_principal.panel_activo
            ide = panel.entry_id.get()
            categoria = panel.lista_opciones.get()

            self.service_libro.administrar_donacion(ide, categoria)

        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)

    def rechazar_donacion(self):
        try:
            panel = self.GUI_ventana_principal.panel_activo
            ide = panel.entry_id.get()
            panel.limpiar_tabla()

            self.GUI_ventana_principal.mostrar_mensaje(
                self.service_donativo.eliminar_donacion(ide)
            )

            self.recibir_registros(panel)

        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)

    # ===================== LIBROS =====================

    def agregar_libro(self):
        try:
            panel = self.GUI_ventana_principal.panel_activo

            titulo = panel.entry_titulo.get()
            autor = panel.entry_autor.get()
            inventario = panel.entry_inventario.get()
            categoria = panel.entry_categoria.get()

            self.service_libro.registrar_libro(
                titulo,
                autor,
                int(inventario),
                categoria
            )

            self.GUI_ventana_principal.mostrar_mensaje(
                'Registrado con exito!'
            )

            panel.cargar()

        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)