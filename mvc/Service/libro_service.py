from Model.libro_model import Libro
import random


class LibroService:
    def __init__(self, repository):
        self.repo = repository('/Data/Json/file_libro.json', Libro.from_dict)

    def registrar_libro(self,titulo,autor,inventario,id_estante):
        if not titulo.strip():
            raise ValueError('Debe de rellenar los campos')
        if not autor.strip():
            raise ValueError('Debe de rellenar los campos')
        if not id_estante.strip():
            raise ValueError('Debe de rellenar el campo del estante')
        

        #-==-=--=-==-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
        id_aleatorio = random.randint(1,1000)
        nuevo = Libro(id_aleatorio, titulo, autor, inventario, 'Desocupado', id_estante)

        #-==-=--=-==-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

        

