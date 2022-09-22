#!/usr/bin/python3
def uppercase(str):
    result = ""
    for v in str:
        if (ord(v) >= 97 and ord(v) <= 122):
            result += chr(ord(v) - 32)
        else:
            result += v
    print("{}".format(result))
