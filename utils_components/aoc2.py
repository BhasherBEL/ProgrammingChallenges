import collections
import re
from typing import Union
import requests
from datetime import datetime
import os
import numpy as np


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

        ordered_dict = collections.OrderedDict(sorted(kwargs.items(), reverse=True))

        filename = self.file_format.format(".".join(map(str, ordered_dict.values())))
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
                    print(f'Error {req.status_code} when trying to download data from {url}.'
                          f'Please verify your session cookie.')
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
    def analyse(self, numeric=None, monoline=None):
        if numeric is None:
            numeric = self.numeric_mode
        if monoline is None:
            monoline = self.monoline_mode
        if self.raw:
            if numeric == 'auto':
                ratio = len(re.findall('\d', self.raw)) / (len(re.findall('[a-zA-Z0-9]', self.raw)) + 0.01)
                numeric = ratio >= 0.95
                print(f'{round(ratio * 100)}% of data are digits. Analyse as '
                      f'{"numbers" if numeric else "text"}.')

            empty_line_amount = self.raw.count('\n\n')
            monoline = empty_line_amount <= 2
            print(f'{empty_line_amount} empty line(s) found. Analyse as {"monline" if monoline else "multiline"} data.')

        if self.numeric_mode == 'auto' or self.numeric_mode is None:
            self.numeric_mode = numeric

        if self.monoline_mode is None:
            self.monoline_mode = monoline

        if monoline:
            if numeric:
                self.data = np.array(self.parse(self.raw.split('\n')))
            else:
                self.data = np.array(self.raw.split('\n'))
        else:
            if numeric:
                self.data = np.array([self.parse(group.split('\n')) for group in self.raw.split('\n\n')])
            else:
                self.data = np.array([group.split('\n') for group in self.raw.split('\n\n')])

        return self

    @staticmethod
    def parse(group):
        def parse_number(el):
            try:
                return int(el)
            except ValueError:
                try:
                    return float(el)
                except ValueError:
                    return el
        result = np.array([np.array([parse_number(el) for el in re.findall(r'\d+\.\d+|\d+', line)]) for line in group])
        if max([len(by_line) for by_line in result]) == 1:
            return np.array([el for by_line in result for el in by_line])
        else:
            if len(result) == 1:
                return result[0]
            else:
                return result

    def concat_multi(self, sep=''):
        if self.monoline_mode:
            return self.data
        else:
            return list(map(lambda sg: sep.join(sg), self.data))

    def head(self, amount=5):
        insert = f'{min(amount, len(self.data))}/{len(self.data)}'
        print(f'===== HEAD ({insert}) =====')
        for i, el in enumerate(self.data):
            print(el)
            if i == amount - 1:
                break
        print('===================' + '=' * len(insert))
        return self

    def sum(self, fct=None, data=None, display=True):
        if data is None:
            data = self.data
        res = 0
        for el in data:
            if fct is None:
                res += el
            else:
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