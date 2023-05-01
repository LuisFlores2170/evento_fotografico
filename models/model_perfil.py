from database.bd_connexion import connection
from controllers.__init__ import *
import random




class model_perfil:
    
    #--------------------------------------------------------------------------------------------------
    @classmethod
    def register(self, n_usuario, n_contrasenia):
        done = None
        try:
            cursor = connection.cursor()
            cursor.execute(f"""
                INSERT INTO perfil (usuario,contrasenia) 
                VALUES('{n_usuario}', {n_contrasenia});
            """)
            connection.autocommit = True
            done = True
        except:
            done = False
        
        return done
    
    @classmethod
    def get_perfil(self, username = None, password = None):
        done = None
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT id FROM perfil WHERE usuario = '{username}' AND contrasenia = '{password}'")
            id = cursor.fetchone()
            return id
        except Exception as ex:
            raise Exception(ex)
        
        return done