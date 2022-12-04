import re


def analyze(text: str) -> str:
    """Automatically analyzes the content of the letter to Santa Claus.

    Args:
        text (str): Original letter

    Returns:
        str: simplified letter
    """
    age = re.search(r'(\d+)ans', text).group(1)
    name = re.search(r'jem\'?appelle(.+?)(?: |(j\'?ai))', text).group(1)
    address = re.search(r'j\'?habite(.+?)(?:\.|$)', text).group(1)
    gift = re.findall(r'j\'?aimeraisavoirun(.+?)pour', text)

    return f'[Lettre de {name} {age} ans]\nAdresse{address}\nCadeau: {", ".join(gift)}'


print(analyze("BonjourjemappelleMatheojai6ansetjaimeraisavoirunvelopour pouvoiraller me balader. ensuite j'aimerais bien une nouvelle console nintendo pourjoueràpokemonbleu que je n'ai pas aussi. Par contre j'ai déjà le jeu doncpasbesoin merciperenoel j'habite rue des papillons"))
print('\n')
print(analyze("Cetteannéejaimeraisavoiruntelephonepour m'amuser,jem'appelleClara etjai bientot5anset jaiété tres sage, jaimeraisavoirunchatpourmamuseravec lui ça me fera tres plaisir. j'habite avenue des marmottes"))
print('\n')
print(analyze("Salut papa noel, c'est moi jemappelleElsaj'ai 4ans et j'habite route des papillons. jaimeraisavoirunboite de legopour constructure plein de choses ! merci papa noeletaussi sion peutavoirun deuxiemecadeau jaimeraisavoiruncamion de pompierpourjouer avec mon frere il a 5 ans et il s'apel leo."))