import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import re
import numpy as np
import os
import time


class AOC(object):
    sample_url = 'https://adventofcode.com/{year}/day/{day}'
    input_url = f'{sample_url}/input'
    file_format = 'input.{year}.{day}.{type}.txt'
    fake_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://adventofcode.com/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
    }

    def __init__(self, date=datetime.today(), session='', d=True):
        self.cookies = {'session': session}
        self.date = {'year': date.year, 'day': date.day}
        self.d = d
        self.sample = None
        self.input = None

    def debug(self, *args):
        if self.d:
            print(*args)

    def verify_session(self, year=2020, day=1):
        return requests.get(AOC.sample_url.format(year=year, day=day), cookies=self.cookies).status_code == 200
    
    def get_sample_url(self):
        return AOC.sample_url.format(**self.date)
    
    def get_input_url(self):
        return AOC.input_url.format(**self.date)

    def try_download(self, url):
        print(url)
        req = requests.get(url, cookies=self.cookies, headers=AOC.fake_headers)
        if req.status_code != 200 or req.text.startswith('<!DOCTYPE html>'):
            if req.status_code in [400, 500]:
                self.debug(f'Error {req.status_code} when trying to download data from {url}.'
                        f'Please verify your session cookie.')
            else:
                self.debug(f'Error {req.status_code} when trying to download data from {url}. Message: "{req.text}".')
            return False
        else:
            return req.text

    def download_sample(self):
        if (content := self.try_download(self.get_sample_url())):
            soup = bs(content, 'html.parser')
            samples = soup.find_all('code')
            return Data('\n'.join(map(lambda x: x.text, samples)))
        else:
            print('Error when trying to download data from', url, ': found file is empty.')

    def download_input(self):
        if (content := self.try_download(self.get_input_url())):
            return Data(content)
        else:
            print('Error when trying to download data from', url, ': found file is empty.')

    def get_data(self, force=False):
        if not os.path.exists('data'):
            os.mkdir('data')

        sample_path = os.path.join('data', AOC.file_format.format(**self.date, type='sample'))
        input_path = os.path.join('data', AOC.file_format.format(**self.date, type='input'))

        if not force and os.path.exists(sample_path) and os.path.exists(input_path):
            self.debug('Local file found.')
            self.sample = Data.from_file(sample_path)
            self.input = Data.from_file(input_path)
        else:
            self.debug('Downloading and saving data.')
            self.sample = self.download_sample().to_file(sample_path)
            time.sleep(1)
            self.input = self.download_input().to_file(input_path)

        return self

    def analyze(self, **kwargs):
        _, numeric, monoline = self.input.analyze(**kwargs, get_methods=True)
        self.sample.analyze(numeric=numeric, monoline=monoline)

        return self
            

class Data(object):
    @staticmethod
    def from_file(path):
        with open(path, 'r') as file:
            return Data(file.read())

    def __init__(self, raw, d=True):
        self.raw = raw
        self.data = raw
        self.d = d

    def debug(self, *args):
        if self.d:
            print(*args)

    def to_file(self, path):
        with open(path, 'w') as file:
            file.write(self.raw)

        return self

    def analyze(self, numeric=None, monoline=None, get_methods=True):
        if self.raw:
            if numeric is None:
                ratio = len(re.findall('\d', self.raw)) / (len(re.findall('[a-zA-Z0-9]', self.raw)) + 0.01)
                numeric = ratio >= 0.95
                self.debug(f'{ratio:.0%}% of data are digits. Analyse as '
                      f'{"numbers" if numeric else "text"}.')

            if monoline is None:
                empty_line_amount = self.raw.count('\n\n')
                monoline = empty_line_amount <= 2
                self.debug(f'{empty_line_amount} empty line(s) found. Analyse as {"monline" if monoline else "multiline"} data.')

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

        if get_methods:
            return self, numeric, monoline
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

    def head(self, amount=5):
        insert = f'{min(amount, len(self.data))}/{len(self.data)}'
        print(f'===== head ({insert}) =====')
        for i, el in enumerate(self.data):
            print(el)
            if i == amount - 1:
                break
        print('===================' + '=' * len(insert))
        return self
