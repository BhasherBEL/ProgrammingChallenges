import re

def valid(p):
    data = {}
    for el in re.split(' |\n', p):
        try:
            k,v = el.split(':')
            data[k] = v
        except:
            print(el)
    return 'byr' in data and data['byr'].isdigit() and 1920 <= int(data['byr']) <= 2002\
    and 'iyr' in data and data['iyr'].isdigit() and 2010 <= int(data['iyr']) <= 2020\
    and 'ecl' in data and data['ecl'] in ['amb','blu','brn','gry','grn', 'hzl', 'oth']\
    and 'pid' in data and data['pid'].isdigit() and len(data['pid']) == 9 \
    and 'eyr' in data and data['eyr'].isdigit() and 2020 <= int(data['eyr']) <= 2030\
    and 'hcl' in data and re.match('^#[0-9a-f]{6}$', data['hcl'])\
    and 'hgt' in data \
    and ((data['hgt'][-2:] == 'cm' and data['hgt'][:-2].strip().isdigit() and 150 <= int(data['hgt'][:-2].strip()) <= 193)\
    or (data['hgt'][-2:] == 'in' and data['hgt'][:-2].strip().isdigit() and 59 <= int(data['hgt'][:-2].strip()) <= 76))

with open('input4.txt', 'r') as file:
    pp = file.read().split('\n\n')

isvalids = list(map(valid, pp))
valids = list(filter(lambda x: x, isvalids))
print(len(valids), len(isvalids))