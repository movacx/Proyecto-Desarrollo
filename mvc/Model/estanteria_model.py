class Estanteria: 
    def __init__(self, num_estante:str, titulo:str)->None:
        self.num_estante = num_estante
        self.titulo = titulo

    def __str__(self):
        return f'{self.num_estante} {self.titulo}'
    
    def get_id(self):
        return self.num_estante


    def to_dict(self)->dict:
        return {
            'Estante N°':self.num_estante,
            'Titulo':self.titulo
        }
    
    def from_dict(data:dict)->Estanteria:
        return Estanteria(
            num_estante=data['Estante N°'],
            titulo=data['Titulo']
        )


    #La idea es crear una estanteria virtual o verlo asi, este sistema se usara en una biblioteca no?
    #Lo que quiero decir es que si hay un objeto estanteria en la vida real y tengo mi sistema en la biblioteca y ocupo o necesito saber donde
    #saber en que repisa, estanteria va a estar mi fockin libro reviso en el objeto estanteria y me dira en que numero de estanteria
    #va a estar ademas va haber un json solo para esto obviamente.
    #y ahi va a estar, ahora en el modulo 8 que es busqueda creo que ahi se podria implementar esta funcion.
    #Lo escribo para no perderme.