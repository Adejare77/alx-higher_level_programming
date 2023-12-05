#!/usr/bin/python3
""" File Handling """


def write_file(filename="", text=""):
    """ returns the number of characters written in a file """
    with open(filename, 'w', encoding='utf-8') as fw:
        return fw.write(text)
