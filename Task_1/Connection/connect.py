from peewee import *

# Connect to a MySQL database on network.
mysql_db = MySQLDatabase(
    'rybin_task',
    user='rybin_task',
    password='111111',
    host='10.11.13.118',
    port=3306
)

if __name__ == "__main__":
    # проверить подключение
    print(mysql_db.connect())

