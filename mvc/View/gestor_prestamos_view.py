import tkinter as tk
class GestorPrestamo:
    def __init__(self, enlace_ventana, controller):
        self.manejo_controller = controller
        self.ventana = enlace_ventana
        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.pack(side='right',fill='both',expand=True)
        self.contenedor.configure(bg='skyblue')


