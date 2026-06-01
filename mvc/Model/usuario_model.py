#archivo cliente_model

class Usuario:
    def __init__(self, identificador:str, nombre:str, correo:str, passw:str, rol:str, ped:str) -> None:
        self.identificador = identificador
        self.nombre = nombre
        self.correo = correo
        self.passw = passw
        self.rol = rol
        self.ped = ped

    def __str__(self) -> str:
        return f'{self.identificador} | {self.nombre} | {self.correo} | {self.rol}'

    def get_id(self):
        return self.identificador

    def to_dict(self) -> dict:
        return {
            'Cliente': self.identificador,
            'Nombre': self.nombre,
            'Correo': self.correo,
            'Contraseña': self.passw,
            'Rol': self.rol,
            'Ped': self.ped
        }
    
    def from_dict(data: dict) -> Usuario:
        return Usuario(
            identificador=data['Cliente'],
            nombre=data['Nombre'],
            correo=data['Correo'],
            passw=data['Contraseña'],
            rol=data['Rol'],
            ped=data['Ped']
        )
