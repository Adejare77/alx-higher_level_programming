#!/usr/bin/python3
""" Handling Files """
import sys

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as fr:
        #file = f.read()
        sys.stdout.write(fr.read())
