from Task_3.Models.BaseModel import *


class ShopingList(BaseModel):
    id = PrimaryKeyField()
    product = CharField()
    quantity = IntegerField()
    bought = BooleanField(default=False)

if __name__ == "__main__":
    mysql_db.create_tables([ShopingList])