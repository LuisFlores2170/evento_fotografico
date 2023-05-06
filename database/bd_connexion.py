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
        host='ec2-54-211-177-159.compute-1.amazonaws.com',
        user='dngecpoomqhkgz',
        password='8ecd99476966736ff7e4fb8205fe986f35d9e436dbe5d6b7f236f16196ff90ce',
        database='d5m1l1mlnh5md0'
    )
    connection.autocommit = True
    print("Conexión exitosa.")
    cursor = connection.cursor()


except DatabaseError as ex:
    print("Error durante la conexión: {}".format(ex))