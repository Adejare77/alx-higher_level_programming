#!/usr/bin/python3
""" File Handling """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file

        Args:
            text(str) = text to be written in the file
            filename = name of the file

        Return:
            the number of characters written
    """
    with open(filename, 'a', encoding='utf-8') as fa:
        return fa.write(text)
