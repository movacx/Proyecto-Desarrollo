from Model.libro_model import Libro

class LibroService:
    def __init__(self, repository):
        self.repo = repository('/Data/Json/file_libro.json', Libro.from_dict)

    def registrar_libro(self):
        pass