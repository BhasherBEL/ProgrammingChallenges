import re


class Parse:
    @staticmethod
    def one_line_dict(line: str) -> dict:
        """ Parse a one-line dict into real dict object.

        Args:
            line: String to parse

        Returns:
            Dictionary of parsed values
        """
        return {k.strip(): v.strip() for k, v in re.findall(r'^([^,]*?): ?(.+?) ?$', line.strip().replace(',', '\n'), flags=re.MULTILINE)}
