def backtracking(recipes, recipe, ingredients):
    """
    Return valid recipe.
    :param recipe: list of list of strings
    :param ingredients: list of strings
    :return:
    """
    if len(recipe) == len(ingredients):
        recipes.append(recipe[:])
        return
    for ingredient in ingredients[len(recipe)]:
        recipe.append(ingredient)
        backtracking(recipes, recipe, ingredients)
        recipe.pop()


def gen_all_recipes(ingredients):
    recipes = []
    backtracking(recipes, [], ingredients)
    return recipes


if __name__ == "__main__":
    ingredients = [["flour1", "flour2", "flour3"], ["cream1", "cream2"],
                   ["fruit1", "fruit2", "fruit3", "fruit4", "fruit5", "fruit6"]]
    print(gen_all_recipes(ingredients))

