class Usuario:
    def __init__(self, identificador:str, nombre:str, correo:str, passw:str, rol:str, ped:str)->None:
        self.identificador = identificador
        self.nombre = nombre
        self.correo = correo
        self.passw = passw
        self.rol = rol
        self.ped = ped
        
    def get_id(self):
        return self.identificador

    def get_nombre(self)->str:
        return self.nombre
    
    def get_correo(self):
        return self.correo
    
    def get_passw(self):
        return self.passw

    def setPassword(self, nueva_contraseña)->None:
        self.passw = nueva_contraseña

    def get_ped(self):
        return self.ped

    def __str__(self)->str:
        return f'Nombre: {self.nombre} {self.correo}'
    