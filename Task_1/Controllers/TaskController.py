from Task_1.Models.Tasks import Tasks
from Task_1.Models.TaskModel import Task
class MyTasks:
    '''
    : Управлять списком задач с полями: id, задача, статус (выполнено/невыполнено)

    '''

    # def __init__(self):
    #     '''
    #     Конструктор в котором задаю атрибуты список дел и идентификаторы дел
    #     список дел состоит из словерей
    #     '''
    #     self.__tasks = [
    #         {"id": 1, "task": "Купить молоко", "completed": False},
    #         {"id": 2, "task": "Сделать уроки", "completed": True}
    #     ] # Атрибут класса - список с двумя Делами
    #     self.id = 3 #Атрибут класса - для автоматического создания id

    # Методы CRUD - Create, Read, Update, Delete
    obj = Tasks()
    @classmethod
    def add(cls,task):
        '''
        Создаёт новое дело в виде словаря {"id": 1, "task": "Купить молоко", "completed": False}
        И добаляет в сисок атрибута self.tasks
        :Params
            task(str): Дело в виде строки
            id(int): создаётся автоматически с помошью атрибута self.id
            completed(boolean):  автоматически присваивается False
        :Returns:
            True
        '''
        # self.tasks.append(
        #     {
        #         "id": self.id,
        #         "task": task,
        #         "completed": False
        #     }
        # )
        # self.id +=1 # Увелить на 1, следующий id будет на 1 больше
        cls.obj.tasks = task
        return True
    # показать все - Read

    @classmethod
    def get(cls):
        return cls.obj.tasks

    @classmethod
    def completed(cls,id):
        '''
        Меняет значения completed на True у словаря с id == id из аргумента
        :Params id: Словарь с данным id
        :Returns:
            Task - словарь
        '''
        for dict in cls.get():
            if dict['id'] == id:
                dict['completed'] = True
                return dict
    # Удалить
    @classmethod
    def delete(cls,id):
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)
if __name__ == "__main__":
    # task = Task_1()
    # print(task.tasks)
    # task.add("Сходить в ЯМК")
    # print(task.tasks)
    # print('Метод изменить статус',task.completed(3))
    # print(task.tasks)
    # task.delete(1)
    # print(task.tasks)
    print(MyTasks.add('WWWW'))
    print(MyTasks.get())
    print(MyTasks.completed(3))
    print(MyTasks.delete(3))
    print(MyTasks.get())