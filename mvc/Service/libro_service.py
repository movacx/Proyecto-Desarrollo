from Model.libro_model import Libro

import random

#archivo libro_service.py

class LibroService:
    def __init__(self, repository):
        self.repo = repository('Data/Json/file_libro.json', Libro.from_dict)

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
        
        

        #-==-=--=-==-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#


        

