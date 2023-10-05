# recipe_repository class
from lib.recipe import*


class Recipe_repository:

    def __init__(self,connection):
        self._connection = connection


    def all(self):
        result = self._connection.execute("SELECT * FROM recipes")
        recipes_list = []
        for field in result:
            recipe = Recipe (field["id"],field ["title"],field ["cook_time"], field ["rating"])
            recipes_list.append(recipe)
        return recipes_list

    def find(self, condition):
        try:
            result = self._connection.execute(f"SELECT * FROM recipes WHERE {condition}")
            return result
        except:
            print ("something went wrong there, check ur self and submitted find condition")