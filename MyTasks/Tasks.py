class Tasks:
    def __init__(self):
        '''
        Конструктор в котором задаю атрибуты список дел и идентификаторы дел
        список дел состоит из словерей
        '''
        self.__tasks = [
            {"id": 1, "task": "Купить молоко", "completed": False},
            {"id": 2, "task": "Сделать уроки", "completed": True}
        ] # Атрибут класса - список с двумя Делами
        self.id = 3 #Атрибут класса - для автоматического создания id

    @property
    def tasks(self):
        '''
            Выводит инфомацию о делах
            :Returns: Список словаоей с делами
        '''
        return self.__tasks
    @tasks.setter
    def tasks(self, task):
        self.tasks.append(
            {
                "id": self.id,
                "task": task,
                "completed": False
            }
        )
        self.id += 1  # Увелить на 1, следующий id будет на 1 больше

