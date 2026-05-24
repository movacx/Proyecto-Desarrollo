from Model.libro_model import Libro
from Model.donacion_model import Donativo

import random

#archivo libro_service.py

class LibroService:
    def __init__(self, repository):
        self.repo = repository('Data/Json/file_libro.json', Libro.from_dict)
        self.repo_donativo = repository('Data/Json/donaciones.json', Donativo.from_dict)


        # self.id_donacion = id_donacion
        # self.fecha_donacion = fecha_donacion
        # self.id_cliente = id_cliente
        # self.nombre_autor = nombre_autor
        # self.titulo_libro = titulo_libro
        # self.cant_libros_donados = cant_libros_donados
        # self.recibido = recibido




    def registrar_libro(self,titulo,autor,inventario,categoria):
        if not titulo.strip():
            raise ValueError('Debe de rellenar los campos')
        if not autor.strip():
            raise ValueError('Debe de rellenar los campos')
        if not categoria.strip():
            raise ValueError('Debe de rellenar el campo del estante')
        if inventario <=0:
            raise ValueError('El inventario a registrar no puede ser menor a 0')
        
        id_aleatorio = random.randint(1,1000)

        while self.repo.existe_id(id_aleatorio):
            id_aleatorio = random.randint(1,1000)

        nuevo = Libro(id_aleatorio, titulo, autor, inventario, 'Disponible', categoria)
        self.repo.agregar(nuevo)


#-==-=--=-==-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
        
        
    def administrar_donacion(self, id,categoria):
        print('La funcion sirve')
        if not categoria.strip():
            raise ValueError('Debe de seleccionar una categoria')
        if not id.strip():
            raise ValueError('Debe de seleccionar un donativo')
        
        objeto_recibido = self.repo_donativo.buscar_id(id)
        objeto_recibido.recibido = True
        self.repo_donativo._save()
        while self.repo.existe_id(id):
            id = random.randint(2000,30000)



        titulo = objeto_recibido.titulo_libro
        autor = objeto_recibido.nombre_autor
        inventario = objeto_recibido.cant_libros_donados

        nuevo = Libro(id,titulo,autor,inventario,'Disponible',categoria)
        self.repo.agregar(nuevo)
        #-==-=--=-==-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#


        

