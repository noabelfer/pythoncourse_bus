from backend import CocktailIdeas

def create_instance(ingredients):
    cheers = CocktailIdeas(ingredients)
    return cheers

def present_menu (cheers : CocktailIdeas):
    cheers.menu = cheers.update_menu()
    p_list = []
    for index, drink in enumerate(cheers.menu):
        p_list.append(f"{index}. {drink}")
    return "\n".join(p_list)

def present_recipe(cocktail_num, cheers : CocktailIdeas):
    cheers.update_cocktail_name(cocktail_num)
    cheers.create_recipe()
    return cheers.display_recipe()