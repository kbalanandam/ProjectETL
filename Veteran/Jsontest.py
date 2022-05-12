from Config import dbConfig,fileConfig
import json
import dbAuth
import mysql.connector
from mysql.connector import Error
import test
Config = json.dumps(dbConfig,sort_keys=True,indent=4)
fileConfig = json.dumps(fileConfig,sort_keys=True,indent=4)





a=dbAuth.dbconnect(host=dbConfig['host'],database=dbConfig['database'],user=dbConfig['user'],password=dbConfig['password'])
print(a)

b=test.A()
print(b.foo())








