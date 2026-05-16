class Libro:
    def __init__(self, id_libro:str, titulo:str, autor:str, inventario:int, estado_prestamo:bool,id_estante)->None:
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.inventario = inventario
        self.estado_prestamo = estado_prestamo
        self.id_estante = id_estante

    def get_id(self):
        return self.id_libro

    def __str__(self)->str:
        return f'{self.id_libro}{self.titulo}{self.autor}{self.inventario}{self.estado_prestamo}{self.id_estante}'

    def to_dict(self)->dict:
        return {
            'Libro N°':self.id_libro,
            'Titulo':self.titulo,
            'Autor':self.autor,
            'Stock':self.inventario,
            'Estado':self.estado_prestamo,
            'Estante':self.id_estante
        }
    
    @classmethod
    def from_dict(data:dict)->Libro:
        return Libro(
            id_libro=data['Libro N'],
            titulo=data['Titulo'],
            autor=data['Autor'],
            inventario=data['Estado'],
            id_estante=data['Estante']
        )