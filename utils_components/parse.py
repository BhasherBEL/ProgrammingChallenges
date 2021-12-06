from __future__ import annotations

import re
import typing


class Parse:
    @staticmethod
    def one_line_dict(line: str) -> dict:
        """ Parse a one-line dict into real dict object.

        Args:
            line: String to parse

        Returns:
            Dictionary of parsed values
        """
        return {k.strip(): v.strip() for k, v in
                re.findall(r'^([^,]*?): ?(.+?) ?$', line.strip().replace(',', '\n'), flags=re.MULTILINE)}

    @staticmethod
    def parse_split(data: list, sep: str = None, /, parse=int, strict=False, maxsplit: int = -1) -> typing.Generator:
        for line in data:
            yield Parse.try_parse(line.split(sep, maxsplit))

    @staticmethod
    def try_parse(data: [str | list], parse=int, strict=False) -> [typing.Any | list]:
        if isinstance(data, list):
            for el in data:
                try:
                    yield parse(el)
                except ValueError:
                    if strict:
                        continue
                    yield el
        else:
            try:
                yield parse(data)
            except ValueError:
                if strict:
                    yield
                yield data

    @staticmethod
    def iter_parse(data, f=int):
        for el in data:
            yield f(el)
