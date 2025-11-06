from Task_1.Connection.connect import *

class BaseModel(Model):
    class Meta:
        database = mysql_db