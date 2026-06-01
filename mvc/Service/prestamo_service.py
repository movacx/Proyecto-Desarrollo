from Model.prestamo_model import Prestamo
from datetime import datetime
import random


class ServicePrestamo:
    def __init__(self, repository, service_libro):
        self.repo_prestamo = repository(
            'Data/Json/file_prestamos.json',
            Prestamo.from_dict
        )
        self.service_libro = service_libro

    def registrar_prestamo(self, id_libro, id_cliente):
        if not id_libro.strip():
            raise ValueError('No se ha podido cargar el id del libro, vuelva a intentarlo.')
        if not id_cliente.strip():
            raise ValueError('No se ha encontrado ningun cliente asociado')

        id_prestamo = random.randint(1, 500)

        while self.repo_prestamo.existe_id(id_prestamo):
            id_prestamo = random.randint(1, 500)

        fecha_prestamo, fecha_devolucion = self.sacar_fechas()

        nuevo_prestamo = Prestamo(
            id_prestamo,
            id_libro,
            id_cliente,
            fecha_prestamo,
            fecha_devolucion,
            False,
            True
        )

        exito = self.repo_prestamo.agregar(nuevo_prestamo)
        if exito:
            return 'Solicitado Correctamente!'
        else:
            return 'Error interno.'

    def devolver_libro(self, id_prestamo):
        if not id_prestamo.strip():
            raise ValueError('Debe de rellenar el campo')

        exito = False

        for items in self.repo_prestamo.listar():
            if str(items.id_prestamo) == str(id_prestamo):
                items.set_estado(False)
                exito = self.repo_prestamo._save()

        if exito:
            return 'Gracias por trabajar con nosotros.'
        else:
            return 'Error interno.'

    def mostrar_prestamos_cliente(self, dni):
        resultado = []

        for items in self.repo_prestamo.listar():
            if items.id_cliente == dni:
                resultado.append(items)

        return resultado

    def buscar_morosos(self, estado: bool):
        encontrados = self.repo_prestamo.listar()
        resultado = []

        for items in encontrados:
            if estado:
                if items.moroso == True:
                    resultado.append(items)
            else:
                if items.moroso == False:
                    resultado.append(items)

        return resultado

    def sacar_fechas(self):
        fecha_prestamo = datetime.now().strftime('%d/%m/%Y')

        dia = int(fecha_prestamo[0:2])
        mes = int(fecha_prestamo[3:5])
        anio = int(fecha_prestamo[6:10])

        dia_devolucion = dia + 7

        if dia_devolucion > 31:
            dia_devolucion -= 31
            mes += 1

        if mes > 12:
            mes = 1
            anio += 1

        fecha_devolucion = f'{dia_devolucion:02d}/{mes:02d}/{anio}'

        return fecha_prestamo, fecha_devolucion

    def mostrar_libros(self):
        return self.service_libro.listar_libros()

    def accion_filtrar(self, categoria):
        return self.service_libro.filtrar_categoria(categoria)

    def accion_buscar_libro(self, titulo):
        return self.service_libro.buscar_libro(titulo)

    def listar_prestamos(self):
        return self.repo_prestamo.listar()
        

        
        
