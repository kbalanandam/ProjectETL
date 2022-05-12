
import mysql.connector
from mysql.connector import Error

def dbconnect(**dbconfig):

    connection = mysql.connector.connect(host=dbconfig['host'],
                                         database=dbconfig['database'],
                                         user=dbconfig['user'],
                                         password=dbconfig['password'])


    if connection.is_connected():
        return 1
    else:
        return 0
if __name__=='__main__':
    dbconnect()






