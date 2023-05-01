from database.bd_connexion import *
from controllers.__init__ import *
import random

class model_client:

    @classmethod
    def register(self, id_perfil = None):
        done = None
        try:
            db_register(f"""
                INSERT INTO cliente (id_perfil,fotos_compradas) 
                VALUES({id_perfil},0);
            """)
            done = True
        except:
            done = False
        return done
    
    