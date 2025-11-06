from Task_12.Models.Recipe import Recipe


class RecipeController:
    obj = Recipe()

    @classmethod
    def get(cls):
        return cls.obj.recipes

    @classmethod
    def add(cls,name,cooking_time,difficulty, *ingredients):
        # new_ingredients = []
        # for elemnt in ingredients:
        #     new_ingredients.append(elemnt)
        # new_new_ingredients =  [element for element in ingredients]
        dict = {
            'name' : name,
            'ingredients' : list(ingredients),
            'cooking_time' : cooking_time,
            'difficulty' : difficulty
        }
        cls.obj.recipes = dict
        return dict

if __name__ == "__main__":
    print(RecipeController.get())
    print(RecipeController.add(
        "Яичница",
        7,
        'легкая',
        'яйцо', 'лук','масло'
    ))
    print(RecipeController.get())