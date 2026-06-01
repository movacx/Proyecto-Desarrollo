import tkinter as tk
from tkinter import ttk


class ReportesAdmin:
    def __init__(self, contenedor_padre, controller):
        self.controller = controller

        self.contenedor = tk.Frame(contenedor_padre, bg="#EDEDED")
        self.contenedor.pack(fill="both", expand=True)

        tk.Label(
            self.contenedor,
            text="Reporte Histórico Administrativo",
            font=("Arial", 13, "bold"),
            bg="#EDEDED"
        ).pack(fill="x", pady=10)

        self.tabla = ttk.Treeview(
            self.contenedor,
            columns=("concepto", "cantidad"),
            show="headings",
            height=10
        )

        self.tabla.heading("concepto", text="Concepto")
        self.tabla.heading("cantidad", text="Cantidad")

        self.tabla.column("concepto", width=450, anchor="w")
        self.tabla.column("cantidad", width=150, anchor="center")

        self.tabla.pack(fill="x", padx=20, pady=20)

        self.cargar_reporte()

    def cargar_reporte(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        datos = self.controller.leer_reporte_historico()

        filas = [
            ("Libros registrados manualmente", datos["libros_registrados"]),
            ("Donaciones aprobadas", datos["donaciones_aprobadas"]),
            ("Donaciones rechazadas", datos["donaciones_rechazadas"]),
            ("Préstamos registrados", datos["prestamos_registrados"]),
            ("Usuarios activos", datos["usuarios_activos"])
        ]

        for fila in filas:
            self.tabla.insert("", "end", values=fila)