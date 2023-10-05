#recipe class

class Recipe:

    def __init__(self, id, title, cook_time, rating):
        self.id = id
        self.title = title
        self.cook_time = cook_time
        self.rating = rating

    def __eq__(self, other):

        return self.__dict__ == other.__dict__
    
    def __repr__(self):

        return f"Recipe({self.title},{self.cook_time},{self.rating})"
    