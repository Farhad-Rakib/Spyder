import mysql.connector
import _mysql
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='spyder')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
