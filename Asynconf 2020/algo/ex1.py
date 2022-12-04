def distance(puissance: int, reserve: str) -> str:
    """Calculation of the shooting distance

    Args:
        puissance (int): Power of the shot
        reserve (str): Reserve of flakes

    Returns:
        str: Distance reached
    """
    return str(puissance * len(reserve)//2 - 1) + 'm'


print(distance(25, '❄️❄️❄️'))
print(distance(10, '❄️❄️'))
print(distance(80, '❄️❄️❄️❄️'))
