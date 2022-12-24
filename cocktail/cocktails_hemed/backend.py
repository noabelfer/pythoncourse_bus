import requests
import exceptions

class CocktailIdeas:
    def __init__(self, ingredients):
        self.ingredients = [ingredient for ingredient in ingredients.split(", ")]
        self.menu = []
        self._recipe = []

    def _create_single_menu(self, ingredient):
        """
        Retreives menu of cocktails with specific ingredient
        :param str
        :return list of relevant cocktails
        """

        response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}")
        #make sure response is legitimate

        if response.status_code >= 400:
            raise Exceptions.PageNotFound
        try:
            cocktail_dict = response.json()
        except:
            raise Exceptions.EmptyPage
        cocktail_menu = [cocktail_dict['drinks'][i]['strDrink'] for i in range(len(cocktail_dict['drinks']))]

        return cocktail_menu

    def _create_collated_menu(self):
        """Creates menu of drinks that have multiple ingredients"""
        list_of_menus = [set(self._create_single_menu(ingredient)) for ingredient in self.ingredients]
        collated_menu = list_of_menus[0]
        for i in range(1,len(list_of_menus)):
            collated_menu = collated_menu&list_of_menus[i]

        if len(collated_menu) == 0:
            raise Exceptions.NoCocktail

        return list(collated_menu)

    def update_menu(self):
        """
        checks which menu creator should be used and implements it
        :return:
        """
        if len(self.ingredients) == 1:
            self.menu = self._create_single_menu(self.ingredients[0])
        if len(self.ingredients) > 1:
            self.menu = self._create_collated_menu()
        return self.menu

    def update_cocktail_name(self, cocktail_num):
        if int(cocktail_num) in range(len(self.menu)):
            self.cocktail_name = self.menu[int(cocktail_num)][1]
        else:
            raise Exceptions.InvalidInput
        return self.cocktail_name

    def create_recipe(self):
        """
        retrives recipe for cocktail from API
        """
        response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={self.cocktail_name}")

        if response.status_code >= 400:
            raise Exceptions.PageNotFound

        #reach relevant dictionary
        drinks_dict = response.json()['drinks'][0]

        instructions = drinks_dict["strInstructions"]
        supplies = [drinks_dict[f"strIngredient{i}"] for i in range(1,16) if drinks_dict[f"strIngredient{i}"]]
        amounts = [drinks_dict[f"strMeasure{i}"] for i in range(1, len(supplies))]
        supplies_and_amounts = [(supplies[h], amounts[h]) for h in range(0,len(amounts))]
        self._recipe = [instructions, supplies_and_amounts]
        return self._recipe

    def display_recipe(self):
        """
        creates nice printable version of recipe
        :param recipe (list of lists)
        :return str
        """
        p_list = [f"\n"
                  f"Ingredients: "]
        for ingredient in self._recipe[1]:
            p_list.append(f"{ingredient[0]}: {ingredient[1]}")
        p_list.append(f"\n"
                      f"Instructions:")
        p_list.append(self._recipe[0])
        return "\n".join(p_list)