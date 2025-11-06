from Task_2.Models.Contact import Contact


class ContactController(Contact):
    '''
        Управляет контактами в классе Contact
        методы:
            добавить контакт,
            найти по имени,
            обновить телефон,
            удалить контакт
    '''
    obj = Contact()
    # прокси метод вывода всех контактов
    @classmethod
    def get(cls):
        return cls.obj.contacts

    #добавить контакт
    @classmethod
    def add(cls,name,phone,email):
        cls.obj.contacts = {"name":name,"phone":phone,"email":email}

    # обновить телефон
    @classmethod
    def update_phone(cls,id,new_phone):
        for dict in cls.get():
            if dict['id'] == id:
                dict['phone'] = new_phone

    #удалить контакт
    @classmethod
    def delete(cls,id):
        for dict in cls.get():
            if dict["id"] == id:
                cls.get().remove(dict)

if __name__ == "__main__":

    print(ContactController.get())
    ContactController.add('Василий',"+788888888888", "vas@vas.ru")
    print(ContactController.get())
    ContactController.update_phone(2,"+77777777777")
    print(ContactController.get())
    ContactController.delete(1)
    print(ContactController.get())
