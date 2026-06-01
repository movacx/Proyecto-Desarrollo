from Model.libro_model import Libro
from Model.donacion_model import Donativo
import random

class LibroService:
    def __init__(self, repository):
        self.repo = repository('Data/Json/file_libro.json', Libro.from_dict)
        self.repo_donativo = repository('Data/Json/file_donaciones.json', Donativo.from_dict)
    #-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==[ #Fin constructor ]--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#

    #Funcion: Registro, encargado de registrar el libro \o/
    def registrar_libro(self,titulo,autor,inventario,categoria):
        if not titulo.strip():
            raise ValueError('Debe de rellenar los campos')
        if not autor.strip():
            raise ValueError('Debe de rellenar los campos')
        if not categoria.strip():
            raise ValueError('Debe de rellenar el campo del estante')
        if inventario <=0:
            raise ValueError('El inventario a registrar no puede ser menor a 0')
        
        id_aleatorio = random.randint(1,1000)
        while self.repo.existe_id(id_aleatorio):
            id_aleatorio = random.randint(1001,2000)

        nuevo = Libro(id_aleatorio, titulo, autor, inventario, 'Disponible', categoria)
        return self.repo.agregar(nuevo)

    #---------------------------------------------------------------------------------------#
    #Funcion: Administrar donacion, esta se encarga de registrar oficialmente los libros donados,
    #pasando por un proceso de clasificacion
    def administrar_donacion(self, id, categoria):
        if not categoria.strip():
            raise ValueError('Debe de seleccionar una categoria')
        if not id.strip():
            raise ValueError('Debe de seleccionar un donativo')

        objeto_recibido = self.repo_donativo.buscar_id(id)

        if objeto_recibido is None:
            raise ValueError('No se encontró una donación con ese ID')

        objeto_recibido.recibido = True
        self.repo_donativo._save()

        id_libro = random.randint(2000, 30000)

        while self.repo.existe_id(id_libro):
            id_libro = random.randint(2000, 30000)

        titulo = objeto_recibido.titulo_libro
        autor = objeto_recibido.nombre_autor
        inventario = objeto_recibido.cant_libros_donados

        nuevo = Libro(id_libro, titulo, autor, inventario, 'Disponible', categoria)
        return self.repo.agregar(nuevo)

    #---------------------------------------------------------------------------------------#
    #Funcion: Listar, encargado de pasarle todos los datos, en este caso los libros al controlador.
    def listar_libros(self):
        arreglo = self.repo.listar()
        return arreglo

    #---------------------------------------------------------------------------------------#
    #Funcion: buscar, encargado de pasarle los resultados de busqueda al controlador.
    def buscar_libro(self, titulo_libro):
        lista_libros = self.repo.listar()
        resultado = []
        
        for items in lista_libros:
            if titulo_libro.lower() in items.titulo.lower():
                resultado.append(items)
        if not resultado:
            raise ValueError('No se han encontrado coincidencias')
        return resultado
    
    #---------------------------------------------------------------------------------------#
    #Funcion: filtro de categorias, simple filtra las categoria, las lista y retorna.
    def filtrar_categoria(self, categoria): 
        lista_libros = self.repo.listar()
        resultado = [] #Categoria se obtiene de la opcion del combobox.get()
        
        for items in lista_libros: #Ya hay registros con = [Fantasia, Romance, Drama, Infantil] por ejemplo.
            if items.categoria.lower() == categoria.lower():
                resultado.append(items)
        
        if not resultado:
            raise ValueError('No se han encontrado coincidencias')
        return resultado

    def listar_libros(self):
        return self.repo.listar()