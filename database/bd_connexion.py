#--------------------------------------------------------------------------------------------------

import psycopg2
from psycopg2 import DatabaseError

#--------------------------------------------------------------------------------------------------

def db_register(query = None):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.autocommit = True

#--------------------------------------------------------------------------------------------------

def db_fetchall(query = None):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#--------------------------------------------------------------------------------------------------

def db_fetchone(query = None):
    try:
        cursor = connection.cursor()
        print(query)
        cursor.execute(query)
        data = cursor.fetchone()
        if data != None:
            return data[0]
    except:
        return None
    return None

#--------------------------------------------------------------------------------------------------

try:
    connection = psycopg2.connect(
        host='ec2-3-208-74-199.compute-1.amazonaws.com',
        user='narfdmrxvcsaoe',
        password='3929fbd7efeae68d3e6d41d9b72fa3df8f27d1eb2abcb3f09ac287edad379cae',
        database='d56qlui1mu5fdg'
    )
    connection.autocommit = True
    print("Conexión exitosa.")
    cursor = connection.cursor()


except DatabaseError as ex:
    print("Error durante la conexión: {}".format(ex))