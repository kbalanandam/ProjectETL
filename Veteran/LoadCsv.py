import pandas as pd
import logging
import csv
import os
import sys
import mysql.connector
from mysql.connector import Error
import Config
from Config import dbConfig, fileConfig
from datetime import datetime


def fileload():
    try:
        for x in os.listdir(fileConfig['validpath']):
            if x.endswith(fileConfig['extension']):
                Config.FileCount = Config.FileCount + 1
                # Prints only text file present in My Folder
                try:
                    connection = mysql.connector.connect(host=dbConfig['host'],
                                                         database=dbConfig['database'],
                                                         user=dbConfig['user'],
                                                         password=dbConfig['password'])
                    try:
                        if connection.is_connected():
                            db_Info = connection.get_server_info()
                            print(str(datetime.now()) + ": Connected to MySQL Server version ", db_Info)
                            cursor = connection.cursor()

                        print(str(datetime.now()) + ": Reading file -> ", fileConfig['validpath'] + x)

                        with open(fileConfig['validpath'] + x, "r") as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=fileConfig['delimiter'])
                            for row in csv_reader:
                                cursor.execute(
                                    "INSERT INTO VetaranPlates(PlateState, LicensePlate, StartEffectiveDate, EndEffectiveDate, CreatedDate, CreatedUser, UpdatedDate, UpdatedUser) VALUES(%s, %s, %s, %s, now(),'CsvLoad',now(),'CsvLoad')",
                                    row)
                                connection.commit()

                    except Error as e:
                        print(str(datetime.now()) + ": Error while loading data to MySQL", e)
                        if connection.is_connected():
                            cursor.close()
                            connection.close()
                            print(str(datetime.now()) + ": MySQL connection is closed")

                    if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print(str(datetime.now()) + ": MySQL connection is closed")

                except Error as e:
                    print(str(datetime.now()) + ": Error while connecting to MySQL", e)
                    if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print(str(datetime.now()) + ": MySQL connection is closed")
    except Exception as e:
        print(e)
    finally:
        sys.exit()

if __name__ == '__main__':
    fileload()