from json import JSONDecodeError

from cocktail import *
import pprint


class IngredientError:
    pass


if __name__ == '__main__':
    while True:
        print("*****Hello and welcome to out cocktail party******")
        try:
            ingredient = input("what ingredients do you have:  ")
            ing_list = ingredient.split(",")
            if len(ing_list) > 1:
                ingredient = "&=".join(ing_list)
        except JSONDecodeError:
            continue
        cocktail_dict = search_cocktail(ingredient)
        print(cocktail_dict)
        input_i = int(input("please choose the cocktail number: "))
        drink_name = drink_name(cocktail_dict,input_i)
        choose_cocktail(drink_name)