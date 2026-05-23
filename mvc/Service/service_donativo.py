from Model.donacion_model import Donativo
import random
from datetime import datetime

class DonativoService:
    def __init__(self, repository):
        self.repo = repository('Data/Json/donaciones.json', Donativo.from_dict)


    def registrar_libro(self, autor, titulo, cantidad, cedula_usuario):
        if not autor.strip():
            raise ValueError('Debe de ingresar un autor') 
        if not titulo.strip():
            raise ValueError('Debe de ingresar un titulo')
        if int(cantidad) <= 0:
            raise ValueError('La cantidad a donar no puede ser menor a 0')
        
        id_unico = random.randint(1, 3000)
        while self.repo.existe_id(id_unico):
            id_unico = random.randint(1, 3000)

        fecha = datetime.now().strftime('%Y-%m-%d')
        
        nuevo_donativo = Donativo(id_unico, cedula_usuario, fecha, autor, titulo, int(cantidad), False)
        
        self.repo.agregar(nuevo_donativo)

    def listar_registros(self):
        return self.repo.listar()