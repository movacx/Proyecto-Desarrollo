from Model.donacion_model import Donativo
import random
from datetime import datetime

class DonativoService:
    def __init__(self, repository):
        self.repo = repository('Data/Json/file_donaciones.json', Donativo.from_dict)
    #-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==[ #Fin constructor ]--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#

    #Funcion: Crea una nueva donacion
    def crear_donacion(self, autor, titulo, cantidad, cedula_usuario):
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
        
        exito = self.repo.agregar(nuevo_donativo)
        if exito:
            return 'Agregado con exito'
        else:
            return 'Hubo un error'

    #---------------------------------------------------------------------------------------#
    #Funcion: Busca resultados con cierto id dentro de las donaciones.
    def buscar_registro(self, id):
        return self.repo.mostrar_historial(id)
    
    #---------------------------------------------------------------------------------------#
    #Funcion: Lista todas las donaciones.
    def listar_registros(self):
        return self.repo.listar()
    
    