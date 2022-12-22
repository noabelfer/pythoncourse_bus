from cocktail import *
import pprint

if __name__ == '__main__':
    print("*****greeting******")
    ingredient = input("ingredients:  ")
    ing_list = ingredient.split(",")
    if len(ing_list) > 1:
        ingredient = "&=".join(ing_list)
    cocktail_dict = search_cocktail(ingredient)
    # print(cocktail_dict)
    input_i = int(input("please choose the cocktail number: "))
    drink_name = drink_name(cocktail_dict,input_i)
    choose_cocktail(drink_name)