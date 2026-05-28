from Model.usuario_model import Usuario

class ClienteService:
    def __init__(self, repository):
        self.repo = repository('Data/Json/file_usuarios.json', Usuario.from_dict)
    
    #-=-=-==--==--==--==--=-=-==--==--=-=-=-=-=-=-=-=-=-=-=-=-=-==[ #Fin constructor ]--=-=-==--=-=-=-==-=-=-=--=-=-=-==--=-=-=-==-=--==-=--==-=-=-=--==-=--=-=-=-=-==-=-=-=-=-=-#


    #Funcion: Registro cliente, encargado de registrar al cliente \o/
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
        
        #Validar que no exista el mismo id 
        usuario_existente = self.repo.buscar_id(identificador)
        if usuario_existente is not None:
            raise ValueError('Ya se encontro a un usuario con el mismo DNI')
        
        #Crear el cliente
        nuevo_usuario = Usuario(identificador,nombre,correo,passw,'Usuario',ped)
        exito = self.repo.agregar(nuevo_usuario)
        if exito:
            return 'Agregado con exito'
        else:
            return 'Hubo un error, no se pudo registrar'
    
    #---------------------------------------------------------------------------------------#
    #Funcion: Recuperar, encargado de recuperar la cuenta  del cliente \o/
    def recuperar_cliente(self,correo, nueva_contrasenna, pregunta_seguridad):
        if not correo.strip():
            raise ValueError('El campo es necesario.')
        if not nueva_contrasenna.strip():
            raise ValueError('La contraseña es necesaria.')
        if not pregunta_seguridad.strip():
            raise ValueError('Tiene que responde la pregunta de seguridad!')
        
        usuario_encontrado = None

        for items in self.repo.listar():
            if str(items.correo) == str(correo).strip():
                usuario_encontrado= items

        if usuario_encontrado == None:
            raise ValueError('No se encontro ningun usuario con esa direccion de correo!')

        if str(usuario_encontrado.ped).strip() != str(pregunta_seguridad).strip():
            raise ValueError('La respuesta de seguridad no coincide!')
        
        usuario_encontrado.passw = nueva_contrasenna
        self.repo.modificar(usuario_encontrado)
        return 'Se ha actualizado la contraseña de manera exitosa!'
    
    #---------------------------------------------------------------------------------------#
    #Funcion: Login, encargado de loguear al cliente \o/
    def loguearse(self, correo, contra):
        if not correo.strip():
            raise ValueError('Debe de completar el campo vacio')
        if not contra.strip():
            raise ValueError('Debe de completar el campo vacio')

        #Nota: Aca es para el login, cuando coincidan los datos va abrir la
        #ventana principal y retorna el cliente logueado.
        usuario_encontrado = None
        for items in self.repo.listar():
            if str(items.correo) == str(correo).strip():
                usuario_encontrado = items
                break

        if usuario_encontrado == None:
            raise ValueError('El correo digitado no se encuentra registrado!')
        if str(usuario_encontrado.passw) != str(contra):
            raise ValueError('Contraseña incorrecta!')
        return usuario_encontrado



            
        

        
