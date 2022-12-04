import collections
import re
from typing import Union
import requests
from datetime import datetime
import os


class AOC(object):
    def __init__(
            self,
            today=datetime.today(),
            input_url='https://adventofcode.com/{year}/day/{day}/input',
            data_dir='data',
            file_format='input.{0}.txt',
            session=''
    ):
        self.today = today
        self.input_url = input_url
        self.data_dir = data_dir
        self.file_format = file_format
        self.cookies = {'session': session}
        self.raw = ''
        self.data = ''
        self.monoline_mode = None
        self.numeric_mode = 'auto'

    def verify_session(self):
        return requests.get('https://adventofcode.com/2020/day/1/input', cookies=self.cookies).status_code == 200

    def get_input_url(self, **kwargs):
        return self.input_url.format(**kwargs)

    def get_file(self, force=False, **kwargs):
        if not os.path.exists('data'):
            os.mkdir('data')

        orderedDict = collections.OrderedDict(sorted(kwargs.items(), reverse=True))

        filename = self.file_format.format(".".join(map(str, orderedDict.values())))
        path = os.path.join(self.data_dir, filename)

        if not force and os.path.exists(path):
            print('Local file found.')
            with open(path, 'r') as file:
                self.raw = file.read()
        else:
            url = self.get_input_url(**kwargs)
            req = requests.get(url, cookies=self.cookies)
            if req.status_code != 200:
                if req.status_code in [400, 500]:
                    print(
                        f'Error {req.status_code} when trying to download data from {url}. Please verify your session cookie.')
                else:
                    print(f'Error {req.status_code} when trying to download data from {url}. Message: "{req.text}".')
            else:
                content = req.text.strip()
                if content:
                    with open(path, 'w') as file:
                        file.write(content)
                    print('Data correctly downloaded and saved locally for next usage.')
                    self.raw = content
                else:
                    print('Error when trying to download data from', url, ': found file is empty.')
        return self

    def get_today_file(self, force=False):
        return self.get_file(force=force, year=self.today.year, day=self.today.day)

    # TODO Customise here
    def analyse(self, numeric_mode=None, monoline_mode=None):
        if numeric_mode is None:
            numeric_mode = self.numeric_mode
        if monoline_mode is None:
            monoline_mode = self.monoline_mode
        if self.raw:
            if self.numeric_mode == 'auto':
                ratio = len(re.findall('\d', self.raw)) / (len(re.findall('[a-zA-Z0-9]', self.raw)) + 0.01)
                self.numeric_mode = ratio >= 0.95
                print(
                    f'{round(ratio * 100)}% of data are digits. Analyse as {"numbers" if self.numeric_mode else "text"}.')

            empty_line_amount = self.raw.count('\n\n')
            self.monoline_mode = empty_line_amount <= 2
            print(f'{empty_line_amount} empty line(s) found. Analyse as {"monline" if self.monoline_mode else "multiline"} data.')

            if self.monoline_mode:
                stripped = map(lambda x: x.strip(), self.raw.strip().split('\n'))
                if self.numeric_mode:
                    self.data = [int(x) for x in stripped if is_digit(x)]
                else:
                    self.data = [line for line in stripped if line]
            else:
                stripped = map(lambda x: x.strip(), self.raw.strip().split('\n\n'))
                if self.numeric_mode:
                    self.data = [list(map(int, filter(lambda y: y.isdigit(), x))) for x in stripped]
                else:
                    self.data = list(
                        map(lambda x: list(filter(lambda x: x, map(lambda y: y.strip(), x.split('\n')))), stripped))

        else:
            print('Can\'t perform analyse on non-existant or empty content.')

        return self

    def concat_multi(self, sep=''):
        if self.monoline_mode:
            return self.data
        else:
            return list(map(lambda sg: sep.join(sg), self.data))

    def head(self, amount=5):
        print(f'===== HEAD ({amount}) =====')
        for i, el in enumerate(self.data):
            print(el)
            if i == amount - 1:
                break
        print('===================' + '=' * len(str(amount)))
        return self

    def sum(self, fct, data=None, display=True):
        if data is None:
            data = self.data
        res = 0
        for el in data:
            res += fct(el)
        if display:
            print(f'sum: {res!s}')
        return res


def is_digit(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def head(it: Union[dict, iter], amount: int = 5) -> None:
    if isinstance(it, dict):
        for i, (k, v) in enumerate(it.items()):
            if i >= amount:
                break
            print(k, v)
    elif isinstance(it, iter):
        print(it)