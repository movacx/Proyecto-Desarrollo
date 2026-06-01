import tkinter as tk

from Controller.registro_controller import LoginController
from Controller.usuario_controller import ControladorVentanaPrincipal
from Controller.administrador_controller import ControladorVentanaAdministrativa

from Repository.repositorio import Repository

from Service.cliente_service import ClienteService
from Service.libro_service import LibroService
from Service.donacion_service import DonativoService
from Service.prestamo_service import ServicePrestamo


def main():
    root = tk.Tk()

    # ================= REPOSITORIO =================
    repo = Repository

    # ================= SERVICES =================
    service_cliente = ClienteService(repo)
    service_libro = LibroService(repo)
    service_donativo = DonativoService(repo)
    service_prestamo = ServicePrestamo(repo, service_libro)

    # ================= CONTROLLERS =================
    controller_admin = ControladorVentanaAdministrativa(
        root,
        service_libro,
        service_donativo,
        service_prestamo
    )

    controller_login = LoginController(
        root,
        service_cliente,
        ControladorVentanaPrincipal,
        service_donativo,
        controller_admin,
        service_libro,
        service_prestamo
    )

    root.mainloop()


if __name__ == '__main__':
    main()
    

