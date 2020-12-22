def translate(text: str) -> str:
    """Translates the sentences and gives the hidden meaning.

    Args:
        text (str): Text to translate

    Returns:
        str: Hidden meaning
    """
    words = text.strip(' \n»«').split()

    sapin_count = 0
    for word in words:
        if word == 'sapin':
            break
        sapin_count += 1
    else:
        sapin_count = 0

    gift_count = 0
    for word in words:
        if word == 'cadeau':
            break
        gift_count += 1
    else:
        gift_count = 0

    return gift_count * '🎁' + sapin_count * '🎄'


print(translate('« Mon beau sapin roi des forêts »'))
print(translate('« Je n \'aurais jamais de sapin de noël »'))
print(translate('« Mon sapin est mon premier cadeau de noël »'))
print(translate('« Mon cadeau sapin de noel »'))
