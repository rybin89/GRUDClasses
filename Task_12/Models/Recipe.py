
class Recipe:
    def __init__(self):
        self.__recipes = [
            {
                "id": 1,
                "name": "Борщ",
                "ingredients": [
                    "свекла",
                    "капуста",
                    "мясо"
                ],
                "cooking_time": 120,
                "difficulty": "средняя"
            }
        ]
        self.id = 2
    @property
    def recipes(self):
        return self.__recipes
    @recipes.setter
    def recipes(self,dict):
        dict['id'] = self.id
        self.recipes.append(dict)
        self.id +=1

if __name__ == "__main__":
    rec = Recipe()
    rec.recipes = {
        "name": "Яичница",
        "ingredients": [
            "яйцо",
            "лук",
            "масло"
        ],
        "cooking_time": 7,
        "difficulty": "легкая"
    }
    print(rec.recipes)