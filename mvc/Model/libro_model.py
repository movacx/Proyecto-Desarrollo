#archivo libro_model.py

class Libro:
    def __init__(self, id_libro:str, titulo:str, autor:str, inventario:int, estado_prestamo:bool,categoria)->None:
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.inventario = inventario
        self.estado_prestamo = estado_prestamo
        self.categoria = categoria

    def get_id(self):
        return self.id_libro

    def __str__(self)->str:
        return f'{self.id_libro}{self.titulo}{self.autor}{self.inventario}{self.estado_prestamo}{self.categoria}'

    def to_dict(self)->dict:
        return {
            'Libro N°':self.id_libro,
            'Titulo':self.titulo,
            'Autor':self.autor,
            'Stock':self.inventario,
            'Estado':self.estado_prestamo,
            'Categoria':self.categoria
        }
    
    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            id_libro=data['Libro N°'],
            titulo=data['Titulo'],
            autor=data['Autor'],
            inventario=data['Stock'],
            estado_prestamo=data['Estado'],
            categoria=data['Categoria']
        )
        
    