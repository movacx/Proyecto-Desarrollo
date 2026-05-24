import tkinter as tk

from Controller.login_controller import LoginController
from Controller.controller_ventana_principal import Ventana
from Controller.controller_ventana_adm import VentanaAdministrativa

from Repository.repositorio import Repository

from Service.cliente_service import ClienteService
from Service.libro_service import LibroService
from Service.service_donativo import DonativoService


def main():
    root = tk.Tk()
    # ================= REPOSITORIO =================
    repo = Repository
    # ================= SERVICES =================
    service_cliente = ClienteService(repo)
    service_libro = LibroService(repo)
    service_donativo = DonativoService(repo)

    # ================= CONTROLLERS =================
    controller_admin = VentanaAdministrativa(root,service_libro,service_donativo)
    controller_login = LoginController(root,service_cliente,Ventana,service_donativo,controller_admin)

    root.mainloop()


if __name__ == '__main__':
    main()
    

