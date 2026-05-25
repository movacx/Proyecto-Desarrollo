from Model.prestamo_model import Prestamo

from datetime import datetime
import random

class ServicePrestamo:
    def __init__(self, repository, service_libro):
        self.repo_prestamo = repository('Data/Json/file_prestamos.json', Prestamo.from_dict)
        self.service_libro = service_libro

    def registrar_prestamo(self, id_libro, id_cliente, fecha_devolucion):
        if not id_libro.strip():
            raise ValueError('No se ha podido cargar el id del libro, vuelva a intentarlo.')
        if not id_cliente.strip():
            raise ValueError('No se ha encontrado ningun cliente asociado')
        if not fecha_devolucion.strip():
            raise ValueError('Debe de ingresar una fecha')
        
        id_prestamo = random.randint(1,500)
        while self.repo.existe_id(id_prestamo):
            id_prestamo = random.randint(1,500)

        fecha_prestamo = datetime.strftime('%d/%m/%Y')

        nuevo_prestamo = Prestamo(id_prestamo,id_libro,id_cliente,fecha_prestamo,fecha_devolucion,False)

        self.repo.agregar(nuevo_prestamo)

    def mostrar_libros(self):
        return self.service_libro.listar_libros()

    def accion_filtrar(self, categoria):
        return self.service_libro.filtrar_categoria(categoria)
    
    def accion_buscar_libro(self, titulo):
        return self.service_libro.buscar_libro(titulo)
    

    def buscar_morosos(self, estado:bool):
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

    def listar_prestamos(self):
        return self.repo_prestamo.listar()
    
    

        

        
        
