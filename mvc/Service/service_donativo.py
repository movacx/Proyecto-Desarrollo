from Model.donacion_model import Donativo

class DonativoService:
    def __init__(self, repository):
        self.repo = repository('Data/Json/donativo.py', Donativo.from_dict)
