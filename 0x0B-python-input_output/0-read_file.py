#!/usr/bin/python3
""" Read File """


def read_file(filename=""):
    """ reads a text file (uft8) and prints it to stdout

        Args:
            filename: name of the file to be read
    """
    with open(filename, 'r', encoding='utf-8') as fr:
        print(fr.read(), end="")
