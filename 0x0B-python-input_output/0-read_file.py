#!/usr/bin/python3
""" Handling Files """
import sys


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as fr:
        sys.stdout.write(fr.read())
