from Model.prestamo_model import Prestamo
from datetime import datetime
import random

class ServicePrestamo:
    def __init__(self, repository, service_libro):
        self.repo_prestamo = repository('Data/Json/file_prestamos.json', Prestamo.from_dict)
        self.service_libro = service_libro
    #-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==[ #Fin constructor ]--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#

    #Funcion: Crea un nuevo prestamo
    def registrar_prestamo(self, id_libro, id_cliente):
        if not id_libro.strip():
            raise ValueError('No se ha podido cargar el id del libro, vuelva a intentarlo.')
        if not id_cliente.strip():
            raise ValueError('No se ha encontrado ningun cliente asociado')
        
        #Nota: Generador de Id aleatorio
        id_prestamo = random.randint(1,500)
        while self.repo_prestamo.existe_id(id_prestamo):
            id_prestamo = random.randint(1,500)

        #Creacion del Objeto
        fecha_prestamo, fecha_devolucion = self.sacar_fechas()
        nuevo_prestamo = Prestamo(id_prestamo,id_libro,id_cliente,fecha_prestamo,fecha_devolucion,False,True)

        if self.repo_prestamo.agregar(nuevo_prestamo):
            return 'Solicitado Correctamente!'
        else:
            return 'Error interno.'

    #---------------------------------------------------------------------------------------#
    #Funcion: Utilizada en el panel devolusion, responsable de modificar el estado del prestamo.
    def devolver_libro(self, id_prestamo):
        if not id_prestamo.strip():
            raise ValueError('Debe de rellenar el campo')
        
        for items in self.repo_prestamo.listar():
            if str(items.id_prestamo) == str(id_prestamo):
                items.set_estado(False)
                exito = self.repo_prestamo._save()

        if exito:
            return 'Gracias por trabajar con nosotros.'
        else:
            return 'Error interno.'
    
    #---------------------------------------------------------------------------------------#
    #Funcion: Muestra los prestamos por cada cliente (se filtra por el parametro:dni)
    def mostrar_prestamos_cliente(self, dni):
        resultado = []
        for items in self.repo_prestamo.listar():
            if items.id_cliente == dni:
                resultado.append(items)
        return resultado
    
    #---------------------------------------------------------------------------------------#
    #Funcion: La idea es filtrar los clientes morosos, sin embargo aun no se habilita.
    def buscar_morosos(self, estado:bool):
        encontrados = self.repo_prestamo.listar()
        resultado = []
        for items in encontrados:
            if estado:
                if items.moroso == True:
                    resultado.append(items)
            else:
                if items.moroso == False:
                    resultado.append(items)
        return resultado
    
    #---------------------------------------------------------------------------------------#
    #Funcion: Literalmente se sacan las fechas de este metodo
    #retorna: [fecha_prestamo,fecha_devolucion] - Nota: Tiene limitaciones.
    def sacar_fechas(self):
        fecha_prestamo = datetime.now().strftime('%d/%m/%Y')
        #Dia
        num1= fecha_prestamo[0]
        num2=fecha_prestamo[1]
        #Mes
        num4 = fecha_prestamo[4]
        #annio
        string_annio = f'{fecha_prestamo[6]}{fecha_prestamo[7]}{fecha_prestamo[8]}{fecha_prestamo[9]}'

        #Juntar String
        numero_dia = num1+num2
        numero_mes = num4

        #El plazo para devolver los libros es de 7 dias:
        dia_devolucion = int(numero_dia) + 7

        #Si la fecha supera el 31 sumarle 1 al mes y que reinicie los dias
        if dia_devolucion >= 31:
            dia_devolucion -= 31

            valor = int(numero_mes) + 1
            numero_mes = str(valor)

        fecha_devolucion = f'{dia_devolucion}/{numero_mes}/{string_annio}'

        #Test
        # print(f'Consola registro: Fecha prestamo: {fecha_prestamo} | Fecha devolucion: {fecha_devolucion}')
        return fecha_prestamo, fecha_devolucion

    #-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==[ #Otras funciones.]--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#
    def mostrar_libros(self):
        return self.service_libro.listar_libros()

    def accion_filtrar(self, categoria):
        return self.service_libro.filtrar_categoria(categoria)
    
    def accion_buscar_libro(self, titulo):
        return self.service_libro.buscar_libro(titulo)


        

        
        
