#!/usr/bin/python3
for i in range(9):
    for k in range(i, 10):
        if ((i != k) and (i != 8 or k != 9)):
            print("{}{}".format(i, k), end=", ")
print(f"{i}{k}")
