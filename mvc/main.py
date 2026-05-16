import tkinter as tk

from Controller.login_controller import LoginController
from Repository.repositorio import Repository
from Service.cliente_service import ClienteService

def main():
    root = tk.Tk()
    service = ClienteService(Repository)
    controller = LoginController(root, service)

    root.mainloop()

if __name__ == '__main__':
    main()