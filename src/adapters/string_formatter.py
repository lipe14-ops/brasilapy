from brasilapy.src.interfaces import IAdapter


class StringFormatter(IAdapter):
    """remove chars from string."""

    @staticmethod
    def handler(text: str, banned_chars: list[str] | str) -> str:
        """ Handles string data.

        Params:
            text <string>: text to modify.
            banned_chars <list<string> | string>: characters that will be removed.
        
        Returns <string>:
            formatted string without unwanted chars.
        """

        return ''.join(char for char in text if char not in banned_chars)
