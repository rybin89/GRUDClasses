from Task_4.Models.Movie import *


class MovieController:
    '''
    CRUD
    Функции: добавить фильм, поставить оценку, найти по названию, показать непросмотренные
    '''

    @classmethod
    def add(cls, title, year, rating=0.0, watched=False):
        '''
            добавить фильм
        '''
        Movie.create(
            title = title,
            year = year,
            rating = rating,
            watched = watched
        )
    @classmethod
    def rating_update(cls,id,rating):
        '''поставить оценку'''
        Movie.update({Movie.rating:rating}).where(Movie.id == id).execute()

    @classmethod
    def get_title(cls,title):
        return Movie.select().where(Movie.title == title)

    @classmethod
    def get_watched_false(cls):
        return Movie.select().where(Movie.watched == False)
    @classmethod
    def get(cls):
        return Movie.select()
if __name__ == "__main__":
    # MovieController.add(
    #     'Крёстный отец',
    #     1992
    # )
    # for movie in MovieController.get_title('крёстный отец'):
    #     print(movie.id, movie.title,movie.rating, movie.year,movie.watched)

    for movie in MovieController.get_watched_false():
        print(movie.id, movie.title, movie.rating, movie.year, movie.watched)