import json
import os

from typing import TypeVar, Generic, Callable

#archivo repositorio.py
T = TypeVar('T')

class Repository(Generic[T]):
    def __init__(self, ruta:str, from_dict:Callable[[dict],T])->None:
        
        #-=-==-=--=-=-==-=--==--==--=-=-=-==--=-=-=-==--=-=-==--=-=-==--==--=-=-=-==-#
        self.datos = []
        self.from_dict = from_dict
        #-=-==-=--=-=-==-=--==--==--=-=-=-==--=-=-=-==--=-=-==--=-=-==--==--=-=-=-==-#
        definir_ruta = ruta
        dir_data = os.path.dirname(os.path.abspath(__file__))
        self.file = os.path.abspath(os.path.join(dir_data,'..','..',definir_ruta))# '/Data/Json/file_libro.json'
        #-=-==-=--=-=-==-=--==--==--=-=-=-==--=-=-=-==--=-=-==--=-=-==--==--=-=-=-==-#
        self._load() 
        
        
    #-=-==-=--=-=-==-=--==--==--=-=-=-==--=-=-=-==--=-=-==--=-=-==--==--=-=-=-==-#
    def _load(self)->None:
        if not os.path.exists(self.file):
            return -1
        
        with open(self.file, 'r', encoding = 'utf-8') as file:
            data = json.load(file)

            for items in data:
                self.datos.append(self.from_dict(items))
            return True
        
    def _save(self)->None:
        os.makedirs(os.path.dirname(self.file), exist_ok=True)

        datos_para_guardar = []

        for items in self.datos:
            diccionario = items.to_dict()
            datos_para_guardar.append(diccionario)

        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(datos_para_guardar, file, indent=4, ensure_ascii=False)
            return True

    #-=-==-=--=-=-==-=--==--==--=-=-=-==--=-=-=-==--=-=-==--=-=-==--==--=-=-=-==-#

    def agregar(self, objeto)->bool:
        self.datos.append(objeto)
        return self._save()
    #----------------------------------------
    def listar(self)->list:
        return self.datos
    #----------------------------------------
    def existe_id(self, id: str):
        for item in self.datos:
            if str(item.get_id()) == str(id):
                return True
        return False
    def buscar_id(self, id: str):
        for item in self.datos:
            if str(item.get_id()) == str(id):
                return item
        return None
    def mostrar_historial(self, id):
        resultado = []
        for items in self.datos:
            if str(items.id_cliente) == str(id):
                resultado.append(items)
        return resultado
    #----------------------------------------
    def modificar(self, modificar_obj):
        indice = 0
        for items in self.datos:
            if str(items.get_id()) == str(modificar_obj.get_id()):
                self.datos[indice] = modificar_obj
                self._save()
                return True
            indice += 1
        return False
    #----------------------------------------

    #parte de los reportes
    def generar_reporte_general(self):
        return self.reporte_service.generar_reporte_general()

    def listar_libros(self):
        return self.libro_service.listar_libros()

    def listar_donativos(self):
        return self.donacion_service.listar_donaciones()

    def listar_prestamos(self):
        return self.prestamo_service.listar_prestamos()


        
        
    



                
    