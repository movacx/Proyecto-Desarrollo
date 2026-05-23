from Model.cliente_model import Cliente

#archivo cliente_service


class ClienteService:
    def __init__(self, repository):
        self.repo = repository('Data/Json/file_cliente.json', Cliente.from_dict)
    
    #-==-=--==--==-=-==--==-=-=-=-=--=-==-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-==-=
    def registrar_cliente(self,identificador,nombre,correo,passw,ped):
        if not identificador.strip():
            raise ValueError('El DNI es obligatorio.')
        if not nombre.strip():
            raise ValueError('El nombre es obligatorio.')
        if not correo.strip():
            raise ValueError('El correo es obligatorio.')
        if not passw.strip():
            raise ValueError('Necesita ingresar una contraseña.')
        if not ped.strip():
            raise ValueError('Es una pregunta de seguridad, necesita llenar el campo.')
        
        #-==-=--==--==- Validar que no exista el mismo id -==--==-=-=-=-=--=-==-=--==-=-
        cliente_existente = self.repo.buscar_id(identificador)
        if cliente_existente is not None:
            raise ValueError('Ya se encontro a un usuario con el mismo DNI')
        #-==-=--==--==- Crear el cliente -==--==-=-=-=-=--=-==-=--==-=-

        nuevo_cliente = Cliente(identificador,nombre,correo,passw,'Usuario',ped)
        exito = self.repo.agregar(nuevo_cliente)
        if exito:
            return 'Agregado con exito'
        else:
            return 'Hubo un error, no se pudo registrar'
        
    #-==-=--==--==-=-==--==-=-=-=-=--=-==-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-==-=
    def recuperar_cliente(self,correo, nueva_contrasenna, pregunta_seguridad):
        if not correo.strip():
            raise ValueError('El campo es necesario.')
        if not nueva_contrasenna.strip():
            raise ValueError('La contraseña es necesaria.')
        if not pregunta_seguridad.strip():
            raise ValueError('Tiene que responde la pregunta de seguridad!')
        
        #-==-=--==--==- Cambiar la contra -==--==-=-=-=-=--=-==-=--==-=-\
        cliente_encontrado = None

        for items in self.repo.listar():
            if str(items.correo) == str(correo).strip():
                cliente_encontrado= items

        if cliente_encontrado == None:
            raise ValueError('No se encontro ningun usuario con esa direccion de correo!')

        if str(cliente_encontrado.ped).strip() != str(pregunta_seguridad).strip():
            raise ValueError('La respuesta de seguridad no coincide!')
        
        cliente_encontrado.passw = nueva_contrasenna
        self.repo.modificar(cliente_encontrado)
        return 'Se ha actualizado la contraseña de manera exitosa!'
    
    #-==-=--==--==-=-==--==-=-=-=-=--=-==-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-==-=
    def loguearse(self, correo, contra):
        if not correo.strip():
            raise ValueError('Debe de completar el campo vacio')
        if not contra.strip():
            raise ValueError('Debe de completar el campo vacio')

        #Mas de lo mismo pero aca es para el login, cuando coincidan los datos va abrir la ventana principal y retorna el cliente logueado.
        cliente_encontrado = None
        
        for items in self.repo.listar():
            if str(items.correo) == str(correo).strip():
                cliente_encontrado = items
                break

        if cliente_encontrado == None:
            raise ValueError('El correo digitado no se encuentra registrado!')

        if str(cliente_encontrado.passw) != str(contra):
            raise ValueError('Contraseña incorrecta!')

        return cliente_encontrado



            
        

        
