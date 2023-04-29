#--------------------------------------------------------------------------------------------------

import psycopg2
from psycopg2 import DatabaseError

#--------------------------------------------------------------------------------------------------

try:
    connection = psycopg2.connect(
        host='ec2-3-208-74-199.compute-1.amazonaws.com',
        user='narfdmrxvcsaoe',
        password='3929fbd7efeae68d3e6d41d9b72fa3df8f27d1eb2abcb3f09ac287edad379cae',
        database='d56qlui1mu5fdg'
    )
    print("Conexión exitosa.")
    cursor = connection.cursor()


except DatabaseError as ex:
    print("Error durante la conexión: {}".format(ex))