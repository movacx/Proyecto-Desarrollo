class Usuario:
    def __init__(self, nombre:str, apellido:str)->None:
        self.nombre = nombre
        self.apellido = apellido

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        
    def getNombre(self):
        return self.nombre
    
    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido}'
    
    