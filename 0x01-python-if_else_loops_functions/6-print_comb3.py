#!/usr/bin/python3
for i in range(9):
    for k in range(9):
        if i != k:
            if (i != 8 or k != 9):
                print("{}{}".format(i, k), end=", ")
print(f"{i}{k}")
