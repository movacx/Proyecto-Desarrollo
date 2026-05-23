#archivo: prestamo_model.py

class Prestamo:
    def __init__(self, id_prestamo:str, id_libro:str, id_cliente:str, fecha_prestamo:str, fecha_devolucion:str)->None:
        self.id_prestamo = id_prestamo
        self.id_libro = id_libro
        self.id_cliente = id_cliente
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def get_id(self):
        return self.id_prestamo

    def to_dict(self)->dict:
        return {
            'Prestamo N°':self.id_prestamo,
            'Libro':self.id_libro,
            'Cliente':self.id_cliente,
            'Fecha del Prestamo':self.fecha_prestamo,
            'Fecha de devolución':self.fecha_devolucion
        }

    @classmethod
    def from_dict(data:dict)->Prestamo:
        return Prestamo(
            id_prestamo=data['Prestamo N'],
            id_libro=data['Libro'],
            id_cliente=data['Cliente'],
            fecha_prestamo=data['Fecha del Prestamo'],
            fecha_devolucion=data['Fecha de devolución']
        )
