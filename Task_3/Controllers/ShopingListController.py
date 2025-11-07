# Функции: добавить продукт, отметить купленным, показать некупленное,
# удалить
from Task_3.Models.ShopingList import *


class ShopingListController:

    @classmethod
    def add(cls,product,quantity):
        # вывзываем метод из peewee
        ShopingList.create(product=product,quantity=quantity,bought=False)
    @classmethod
    def update(cls,id,**kwargs):
        ShopingList.update(**kwargs).where(ShopingList.id == id).execute()

    #отметить купленным
    @classmethod
    def bought(cls,id):
        cls.update(id, bought = True)

    @classmethod
    def get(cls):
        return ShopingList.select() # список объектов из таблицы
    @classmethod
    def get_not_bought(cls):
        return ShopingList.select().where(ShopingList.bought == False)

    @classmethod
    def delete(cls,id):
        ShopingList.delete_by_id(id)
if __name__ == "__main__":
    # ShopingListController.add('хлеб',2)
    ShopingListController.update(1,product= 'батон',quantity= 4, bought = True)
    ShopingListController.bought(2)
    print(ShopingListController.get())
    for element in ShopingListController.get():
        print(element.id,element.product,element.quantity, element.bought)
    print('******************')
    for element in ShopingListController.get_not_bought():
        print(element.id, element.product, element.quantity, element.bought)

    ShopingListController.delete(4)