import tkinter as tk
from tkinter import ttk


class ReportesAdmin:
    def __init__(self, contenedor_padre, controller):
        self.controller = controller

        self.contenedor = tk.Frame(contenedor_padre, bg="#F4F4F4")
        self.contenedor.pack(fill="both", expand=True)

        tk.Label(
            self.contenedor,
            text="Módulo de Reportes - Biblioteca",
            font=("Arial", 22, "bold"),
            bg="#F4F4F4",
            fg="#222222"
        ).pack(anchor="w", padx=15, pady=(10, 20))

        self.frame_botones = tk.Frame(self.contenedor, bg="#F4F4F4")
        self.frame_botones.pack(anchor="w", padx=15, pady=5)

        tk.Button(self.frame_botones, text="Reporte general",
                  command=self.reporte_general).grid(row=0, column=0, padx=4)

        tk.Button(self.frame_botones, text="Libros registrados",
                  command=self.reporte_libros).grid(row=0, column=1, padx=4)

        tk.Button(self.frame_botones, text="Donativos registrados",
                  command=self.reporte_donativos).grid(row=0, column=2, padx=4)

        tk.Button(self.frame_botones, text="Préstamos realizados",
                  command=self.reporte_prestamos).grid(row=0, column=3, padx=4)

        self.frame_tabla = tk.Frame(self.contenedor, bg="#F4F4F4")
        self.frame_tabla.pack(fill="both", expand=True, padx=10, pady=15)

        self.tabla = None
        self.reporte_general()

    def crear_tabla(self, columnas, encabezados, anchos):
        if self.tabla is not None:
            self.tabla.destroy()

        self.tabla = ttk.Treeview(
            self.frame_tabla,
            columns=columnas,
            show="headings",
            height=22
        )

        for col, encabezado, ancho in zip(columnas, encabezados, anchos):
            self.tabla.heading(col, text=encabezado)
            self.tabla.column(col, width=ancho, anchor="center")

        self.tabla.pack(fill="both", expand=True)

    def reporte_general(self):
        self.crear_tabla(
            ("dato", "cantidad"),
            ("Dato", "Cantidad"),
            (700, 300)
        )

        reporte = self.controller.generar_reporte_general()

        self.tabla.insert("", "end", values=("Libros registrados", reporte["total_libros"]))
        self.tabla.insert("", "end", values=("Donativos registrados", reporte["total_donativos"]))
        self.tabla.insert("", "end", values=("Préstamos realizados", reporte["total_prestamos"]))

    def reporte_libros(self):
        self.crear_tabla(
            ("id", "titulo", "autor", "categoria", "inventario"),
            ("ID", "Título", "Autor", "Categoría", "Inventario"),
            (80, 280, 220, 180, 120)
        )

        libros = self.controller.listar_libros()

        for libro in libros:
            self.tabla.insert("", "end", values=(
                libro.get_id(),
                getattr(libro, "titulo", ""),
                getattr(libro, "autor", ""),
                getattr(libro, "categoria", ""),
                getattr(libro, "inventario", "")
            ))

    def reporte_donativos(self):
        self.crear_tabla(
            ("id", "cliente", "fecha", "autor", "titulo", "cantidad", "estado"),
            ("ID", "Cliente", "Fecha", "Autor", "Título", "Cantidad", "Estado"),
            (70, 120, 120, 180, 220, 90, 120)
        )

        donativos = self.controller.listar_donativos()

        for donativo in donativos:
            estado = "Aprobado" if donativo.recibido else "Pendiente"

            self.tabla.insert("", "end", values=(
                donativo.id_donacion,
                donativo.id_cliente,
                donativo.fecha_donacion,
                donativo.nombre_autor,
                donativo.titulo_libro,
                donativo.cant_libros_donados,
                estado
            ))
    def reporte_prestamos(self):
        self.crear_tabla(
            ("id", "cliente", "libro", "fecha_prestamo", "fecha_devolucion", "moroso", "estado"),
            ("ID", "Cliente", "Libro", "Fecha préstamo", "Fecha devolución", "Moroso", "Estado"),
            (70, 120, 120, 140, 150, 100, 120)
        )

        prestamos = self.controller.listar_prestamos()

        for prestamo in prestamos:
            moroso = "Sí" if getattr(prestamo, "moroso", False) else "No"
            estado = "Activo" if getattr(prestamo, "estado", False) else "Devuelto"

            self.tabla.insert("", "end", values=(
                getattr(prestamo, "id_prestamo", ""),
                getattr(prestamo, "id_cliente", ""),
                getattr(prestamo, "id_libro", ""),
                getattr(prestamo, "fecha_prestamo", ""),
                getattr(prestamo, "fecha_devolucion", ""),
                moroso,
                estado
            ))