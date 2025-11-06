from Task_1.Models.TaskModel import Task

class TaskController:
    '''
    CRUD
    Через модель Task подключаемся к базе данных таблице task
    и упрвляем данными
    Model.create(), for executing INSERT queries.

    Model.save() and Model.update(), for executing UPDATE queries.

    Model.delete_instance() and Model.delete(), for executing DELETE queries.

    Model.select(), for executing SELECT queries.

    '''
    @classmethod
    def add(cls,task):
        Task.create(task=task) # Добавляем задачу в базу данных c помощью модели Task
    @classmethod
    def get(cls):
        return Task.select() # возвращащает список записей из таблицы в виде объектов
    @classmethod
    def show(cls,id):
       return Task.get_or_none(id) # работает с уникальными полями

    @classmethod
    def update(cls,id,**kwargs):
        Task.update(**kwargs).where(Task.id == id).execute()
    @classmethod
    def delete(cls,id):
        Task.delete_by_id(id)
if __name__ == "__main__":
    # TaskController.add('Отдохнуть')
    list = TaskController.get()
    for task in TaskController.get():
        print(
            task.id, #ид записи
            task.task,
            task.completed
        )
    TaskController.update(3,task = 'Работать',completed=True)
    TaskController.delete(2)
    for task in TaskController.get():
        print(
            task.id, #ид записи
            task.task,
            task.completed
        )