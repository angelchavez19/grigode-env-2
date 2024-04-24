"""Environ"""

import os
from typing import List, Tuple


EQUAL = '='
HASH = '#'


def _read_file(path: str, encoding: str) -> List[str]:
    """Read a file and return it as a list of strings"""

    with open(file=path, mode='r', encoding=encoding) as file:
        return file.read().splitlines()


def _parse_env_line(line: str, index_line: int) -> Tuple[str, str]:
    """Parses a line in the 'KEY=VALUE' format and returns the key (KEY) and the value (VALUE).

    Args:
        line (str): The line in the 'KEY=VALUE' format to parse.
        index_line (int): The index of the line in the file.

    Returns:
        Tuple[str, str]: A tuple with the key (KEY) and the value (VALUE) obtained from the line.

    Raises:
        SyntaxError: If the key-value syntax is invalid or the key is not defined.
    """

    if line.count(EQUAL) != 1:
        raise SyntaxError(
            f'On line {index_line}, the key-value syntax is invalid.')

    key, value = line.split(EQUAL)

    if not key:
        raise SyntaxError(
            f'The key has not been defined on line {index_line}.')

    return key, value


def read_environ(path: str = '.env', encoding: str = 'utf-8'):
    """
    Reads a .env file and sets the environment variables accordingly.

    Args:
        path (str, optional): The path to the .env file. Defaults to '.env'.
        encoding (str, optional): The encoding of the file. Defaults to 'utf-8'.

    Raises:
        IOError: If the file cannot be read.
    """
    file_content = _read_file(
        path=path,
        encoding=encoding)

    for index, line in enumerate(file_content):
        if line.startswith(HASH) or not line:
            continue

        key, value = _parse_env_line(line=line, index_line=index + 1)
        os.environ[key] = value


class Env:
    """Class to handle environment variables.

    Usage:
        from grigodeenv2 import Env, read_environ

        read_environ('.env')

        env = Env()

        SECRET_KEY = env('SECRET_KEY')

        DEBUG = env('DEBUG')
    """

    ENVIRON = os.environ

    def __init__(self) -> None:
        pass

    def __call__(self, key: str) -> str | None:
        return self.ENVIRON.get(key, None)
