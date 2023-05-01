from database.bd_connexion import *
from controllers.__init__ import *
from .model_photographer import *
from .model_client import *



class model_perfil:
    
    #-----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def register(self, n_usuario = None, n_contrasenia = None, type = None):
        done = None

        verified_datas = verified_data(n_usuario,n_contrasenia)
        if verified_datas[3] in [False,None]:
            return verified_datas
        

        try:
            db_register(f"""
                INSERT INTO perfil (usuario,contrasenia,tipo) 
                VALUES('{n_usuario}', '{n_contrasenia}','{type}');
            """)
            done = self.register_type_perfil(type)

            
        except:
            done = False
        
        return validate_operation_performed(done, 'Cuenta creada exitosamente')
    
    #-----------------------------------------------------------------------------------------------------------------------
    
    @classmethod
    def get_perfil(self, username = None, password = None):
        done = None
        msg = None
        try:
            
            id = db_fetchone(f"""
                SELECT id 
                FROM perfil 
                WHERE usuario = '{username}' AND contrasenia = '{password}'"""
            )
            done = True
            msg = 'Login exitoso' if id else 'No se ha encontrado tu perfil en la base de datos'
        except:
            done = False
        return [id, validate_operation_performed(done, msg)]
    

    #-----------------------------------------------------------------------------------------------------------------------
    
    @classmethod
    def register_type_perfil(self, type):
        done = None
        try:
            id_perfil = db_fetchone(f"SELECT MAX(id) FROM perfil")
            if type == 'fotografo':
                done = model_photographer.register(id_perfil)
            else:
                done = model_client.register(id_perfil)
        except:
            done =False

        return done
    
    