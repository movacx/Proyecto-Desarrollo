import json
import os

from View.Frame.admin_libro_frame import RegistroLibro
from View.Frame.admin_donaciones_frame import AdministradorLibros
from View.ventana_administrativa import InterfazAdmin


class ControladorVentanaAdministrativa:
    def __init__(self, root, service_libro, service_donativo):
        self.ventana = root
        self.service_libro = service_libro
        self.service_donativo = service_donativo

        self.ruta_reportes = os.path.join("Repository", "reportes.json")

    def mostrar_ventana(self):
        self.GUI_ventana_principal = InterfazAdmin(
            self,
            self.ventana,
            RegistroLibro,
            AdministradorLibros
        )

    # ========================= REPORTES =========================

    def leer_reporte_historico(self):
        if not os.path.exists(self.ruta_reportes):
            datos = {
                "libros_registrados": 0,
                "donaciones_aprobadas": 0,
                "donaciones_rechazadas": 0,
                "prestamos_registrados": 0,
                "usuarios_activos": 0
            }
            self.guardar_reporte_historico(datos)
            return datos

        with open(self.ruta_reportes, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        campos = [
            "libros_registrados",
            "donaciones_aprobadas",
            "donaciones_rechazadas",
            "prestamos_registrados",
            "usuarios_activos"
        ]

        for campo in campos:
            if campo not in datos:
                datos[campo] = 0

        self.guardar_reporte_historico(datos)
        return datos

    def guardar_reporte_historico(self, datos):
        carpeta = os.path.dirname(self.ruta_reportes)

        if carpeta != "" and not os.path.exists(carpeta):
            os.makedirs(carpeta)

        with open(self.ruta_reportes, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def sumar_reporte(self, campo):
        datos = self.leer_reporte_historico()

        if campo not in datos:
            datos[campo] = 0

        datos[campo] += 1
        self.guardar_reporte_historico(datos)

    def generar_reporte(self):
        datos = self.leer_reporte_historico()

        reporte = (
            "📌 REPORTE HISTÓRICO ADMINISTRATIVO\n\n"
            f"📚 Libros registrados manualmente: {datos['libros_registrados']}\n\n"
            "🤝 DONACIONES\n"
            f"Donaciones aprobadas: {datos['donaciones_aprobadas']}\n"
            f"Donaciones rechazadas: {datos['donaciones_rechazadas']}\n"
        )

        return reporte

    # ========================= DONACIONES =========================

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

    # ========================= LIBROS =========================

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

            self.sumar_reporte("libros_registrados")

            self.GUI_ventana_principal.mostrar_mensaje(
                'Registrado con exito!'
            )
            panel.cargar()

        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)

    def registrar_donacion(self):
        try:
            panel = self.GUI_ventana_principal.panel_activo
            ide = panel.entry_id.get()
            categoria = panel.lista_opciones.get()

            self.service_libro.administrar_donacion(ide, categoria)

            self.sumar_reporte("donaciones_aprobadas")

            self.GUI_ventana_principal.mostrar_mensaje(
                "Donación aprobada con éxito"
            )

            panel.limpiar_tabla()
            self.recibir_registros(panel)

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

            self.sumar_reporte("donaciones_rechazadas")

            self.recibir_registros(panel)

        except Exception as error:
            self.GUI_ventana_principal.mostrar_adv(error)