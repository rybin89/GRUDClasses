from peewee import *

# Connect to a MySQL database on network.
mysql_db = MySQLDatabase(
    'rybin_movies',
    user='rybin_movies',
    password='111111',
    host='10.11.13.118',
    port=3306)
if __name__ == "__main__":
    print(mysql_db.connect())