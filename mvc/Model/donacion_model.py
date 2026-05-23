
#archivo donacion_model.py


class Donativo:
    def __init__(self, id_donacion:str, id_cliente:str, fecha_donacion:str, nombre_autor:str, titulo_libro:str, cant_libros_donados:int, recibido:bool)->None:
        self.id_donacion = id_donacion
        self.fecha_donacion = fecha_donacion
        self.id_cliente = id_cliente
        self.nombre_autor = nombre_autor
        self.titulo_libro = titulo_libro
        self.cant_libros_donados = cant_libros_donados
        self.recibido = recibido

    def get_id(self):
        return self.id_donacion

    def to_dict(self)->dict:
        return {
            'Donación N°':self.id_donacion,
            'Cliente':self.id_cliente,
            'Fecha de donación':self.fecha_donacion,
            'Titulo del libro':self.titulo_libro,
            'Nombre del autor':self.nombre_autor,
            'Cantidad donada': self.cant_libros_donados,
            'Estado':self.recibido
        }
    
    def from_dict(data:dict)->Donativo:
        return Donativo(
            id_donacion=data['Donación N°'],
            id_cliente=data['Cliente'],
            fecha_donacion=data['Fecha de donación'],
            titulo_libro=data['Titulo del libro'],
            nombre_autor=data['Nombre del autor'],
            cant_libros_donados=data['Cantidad donada'],
            recibido=data['Estado']
        )