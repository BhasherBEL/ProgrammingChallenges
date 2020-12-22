def christmas_log(ingredients: str, mix: int) -> str:
    """Created the Christmas log

    Args:
        ingredients (str): list of ingredients
        mix (int): number of mixes to be made

    Returns:
        str: The christmas lgo
    """
    return ingredients[-mix:] + ingredients[:-mix]


print(christmas_log('🥚🍫🧈🧈🧈🥛🍫🍫🥚🥛🍫🥛', 1))
print(christmas_log('🥚🍫🥚🧈🥛🥛🥚🥛🍫', 2))
print(christmas_log('🥚🍫🥚🥚🥚🥚🥚🥚🥚', 7))
