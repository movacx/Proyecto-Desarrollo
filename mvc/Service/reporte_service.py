class ReporteService:
    def __init__(self, libro_service, donacion_service, prestamo_service):
        self.libro_service = libro_service
        self.donacion_service = donacion_service
        self.prestamo_service = prestamo_service

    def contar_lista(self, lista):
        contador = 0

        for _ in lista:
            contador += 1

        return contador

    def generar_reporte_general(self):
        libros = self.libro_service.listar_libros()

        if hasattr(self.donacion_service, "listar_donaciones"):
            donaciones = self.donacion_service.listar_donaciones()
        else:
            donaciones = self.donacion_service.listar_registros()

        prestamos = self.prestamo_service.listar_prestamos()

        return {
            "total_libros": self.contar_lista(libros),
            "total_donativos": self.contar_lista(donaciones),
            "total_prestamos": self.contar_lista(prestamos)
        }