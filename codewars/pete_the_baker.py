
def cakes(recipe: dict, available: dict) -> int:
    """
    Calculate the maximum number of cakes that can be made given a recipe and available ingredients.

    The function checks if all the ingredients required for the recipe are available. If any ingredient is missing, it returns 0. Otherwise, it calculates the maximum number of cakes that can be made based on the available quantities of each ingredient.

    Parameters:
    recipe (dict): A dictionary where keys are ingredient names and values are the amounts needed for one cake.
    available (dict): A dictionary where keys are ingredient names and values are the amounts available.

    Returns:
    int: Maximum number of cakes that can be made.

    Examples:
    >>> cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5})
    2
    >>> cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000})
    0
    >>> cakes({'cream': 200, 'flour': 300}, {'cream': 500, 'flour': 1500, 'sugar': 500})
    2
    """

    if any(ingredient not in available for ingredient in recipe):
        return 0

    return min(available[ingredient] // amount for ingredient, amount in recipe.items())


recipe1 = {"flour": 500, "sugar": 200, "eggs": 1}
available1 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
func1 = cakes(recipe1, available1)  # , 2, 'example #1')

recipe2 = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available2 = {"sugar": 500, "flour": 2000, "milk": 2000}
func2 = cakes(recipe2, available2)  # , 0, 'example #2')
