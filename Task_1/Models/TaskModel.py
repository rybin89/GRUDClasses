from Task_1.Models.BaseModel import *

class Task(BaseModel):
    '''
    Этот клас описывает таблицу task в базе данных
    '''
    id = PrimaryKeyField() # первичный ключ в таблице
    task = CharField() # символьный тип данных (строка) с  максимальным количеством символов 255, не пустое
    completed = BooleanField(default=False) # поле Логическое, по умолчанию False

if __name__ == "__main__":
    mysql_db.create_tables([Task])

    number = IntegerField()
    date = DateField()
    datetime = DateTimeField()
    time = TimeField()