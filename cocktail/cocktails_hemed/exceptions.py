class InvalidInput(Exception):
    pass
class PageNotFound(Exception):
    pass
class EmptyPage(Exception):
    pass
class NoCocktail(Exception):
    def __init__(self, ingredients):
        self.ingredients = ingredients