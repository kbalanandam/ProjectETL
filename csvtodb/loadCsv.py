import logging
import csv
import mysql.connector
from mysql.connector import Error
from Config import dbConfig
from Config import fileConfig
name = __name__


def fileload(filename):
    logging.info('Processing file -> ' + filename)
    try:

        connection = mysql.connector.connect(host=dbConfig['host'],
                                             database=dbConfig['database'],
                                             user=dbConfig['user'],
                                             password=dbConfig['password'])

        if connection.is_connected():
            dbinfo = connection.get_server_info()
            logging.info('Connected to MySQL Server database version ' + dbinfo)
            cursor = connection.cursor()

            with open(fileConfig['validpath'] + filename, "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=fileConfig['delimiter'])
                for row in csv_reader:
                    cursor.execute(
                        "INSERT INTO VetaranPlates(PlateState, LicensePlate, StartEffectiveDate, EndEffectiveDate, CreatedDate, CreatedUser, UpdatedDate, UpdatedUser) VALUES(%s, %s, %s, %s, now(),'loadCsv.load',now(),'loadCsv.load')",
                        row)
                connection.commit()
        return True
    except Error as e:
        logging.error('Program: '+ name +',   Error while connecting to the database: ' + str(e))
        return False
    except csv.Error as e:
        logging.error('Program: ' + name + ', file: {}, {}'.format(filename, e))
        return False





