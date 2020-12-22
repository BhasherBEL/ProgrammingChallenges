import requests
import json

# Download data from api.gouv.fr
data = json.loads(requests.get('https://calendrier.api.gouv.fr/jours-feries/metropole/2020.json').text)


def isChristmas(date: str) -> str:
    """Determines if the given date is Christmas Day

    Args:
        date (str): Date to verify

    Returns:
        str: If the date is Christmas day or not
    """
    if date.count('/') != 2:
        return 'Invalid date'

    day, month, year = date.split('/')

    for date, event in data.items():
        y, m, d = date.split('-')
        if d == day and m == month:
            if event == 'Jour de Noël':
                return '« C\'est noël... »'
                break
            else:
                return '« Pas noël... »'
    else:
        return '« Pas noël... »'


print(isChristmas('25/08/2014'))
print(isChristmas('25/12/2020'))
print(isChristmas('01/01/2019'))
print(isChristmas('25/12/2009'))
print(isChristmas('21/01/2019'))
