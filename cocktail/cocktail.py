import pprint

import requests

def search_cocktail(ingredient) -> dict:
    # ingredient= "lemon"
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}")
    if response.status_code > 400:
        raise Exception
    else:
        cocktail_dict = response.json()
    # print(cocktail_dict)
    for i,v in enumerate(cocktail_dict['drinks']):
        print(i+1,v['strDrink'])
        drinks_menu = [i,v['strDrink']]
    return cocktail_dict

def drink_name(cocktail_dict, input_i)-> str:
    drink_chosen = cocktail_dict['drinks'][input_i-1]['strDrink']
    return drink_chosen

def choose_cocktail(drink_chosen):
    url_chosen = f"http://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_chosen}"
    recipe = requests.get(url_chosen)
    if recipe.status_code < 400:
        drink_info = recipe.json()
        # print(drink_info)
    glass = drink_info['drinks'][0]['strGlass']
    print(f"please choose a {glass}")
    instructions = drink_info['drinks'][0]['strInstructions']
    pprint.pprint(f"instruntions: {instructions}")
    ingredients = []
    for key, value in drink_info['drinks'][0].items():
        if 'strIngredient' in key:
            if value:
                ingredients.append(value)
    # print(ingredients)
    amounts = []
    for key, value in drink_info['drinks'][0].items():
        if 'strMeasure' in key:
            if value:
                amounts.append(value)
    # print(amounts)
    amounts_ingredients = zip(amounts,ingredients)
    amounts_ingredients1 = list(amounts_ingredients)
    # pprint.pprint(amounts_ingredients1)
    print('--------------------')
    for t in amounts_ingredients1:
        print(f"{t[1]}  :  {t[0]}")
    print('--------------------')






    # print(glass)
    # for j in input_i:
    #     print([j,v['strDrink']])




