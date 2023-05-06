from database.bd_connexion import *

message_content = ['style','color:red', 'HA OCURRIDO UN ERROR', None]

def reset_msg():
    return ['style','color:red', 'HA OCURRIDO UN ERROR', None]

#---------------------------------------------------------------------------------------------

def update_msg(color, msg, data):
    message_content[1] = color
    message_content[2] = msg
    message_content[3] = data

#---------------------------------------------------------------------------------------------

def validate_username(username = None):
    print(len(username))
    if len(username)<31:
        update_msg(
            'color:green',
            'Usuario valido',
            True
        )
    else:
        update_msg(
            'color:red',
            'El nombre debe tener menos de 30 caracteres',
            False
        )
    return message_content

#---------------------------------------------------------------------------------------------

def validate_password(password = None):
    if len(password)<11:
        update_msg(
            'color:green',
            'Contraseña valida',
            True
        )
    else:
        update_msg(
            'color:red',
            'La contraseña debe tener menos de 10 caracteres',
            False
        )
    return message_content

#---------------------------------------------------------------------------------------------

def validate_profile_data(username = None, password = None):
    valid_username = validate_username(username)
    if valid_username[3] in [False, None]:
        return valid_username
        
    valid_password = validate_password(password)
    if valid_password[3] in [False, None]:
        return valid_password

    return message_content

#---------------------------------------------------------------------------------------------

def validate_operation_performed(done = None, msg = None):
        if done in [False, None] or msg == None:
            return ['style','color:red', 'Operacion fallida', False]
        return ['style','color:green', msg, True]

#---------------------------------------------------------------------------------------------

def user_available(username = None):
    id = db_fetchone(f"SELECT id FROM perfil WHERE usuario = '{username}'")
    if id == None:
        update_msg(
            'color:green',
            'Usuario disponible',
            True
        )
    else:
        update_msg(
            'color:red',
            'Usuario no disponible',
            False
        )
    return message_content
        
#---------------------------------------------------------------------------------------------
        
def password_available(password = None):
    id = db_fetchone(f"SELECT id FROM perfil WHERE contrasenia = '{password}'")
    if id == None:
        update_msg(
            'color:green',
            'Contraseña segura',
            True
        )
    else:
        update_msg(
            'color:red',
            'Use otra contraseña',
            False
        )
        
    return message_content

#---------------------------------------------------------------------------------------------
    
def already_username_and_password(username = None, password = None):
    valid_username = user_available(username)
    if valid_username[3] in [False, None]:
        return valid_username
        
    valid_password = password_available(password)
    if valid_password[3] in [False, None]:
        return valid_password

    return message_content

#---------------------------------------------------------------------------------------------

def verified_data(n_usuario : str , n_contrasenia: str):
    n_usuario = n_usuario.strip(' ')
    n_contrasenia = n_contrasenia.strip(' ')
    
    if len(n_usuario) > 0 and len(n_contrasenia) > 0:
        
        valid_data = validate_profile_data(n_usuario,n_contrasenia)
        if valid_data[3] in [False, None]:
            return valid_data
            
        already_data = already_username_and_password(n_usuario, n_contrasenia)
        if already_data[3] in [False, None]:
            return already_data
        
    
    return message_content