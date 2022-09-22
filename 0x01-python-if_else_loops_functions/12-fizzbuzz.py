#!/usr/bin/python3
def fizzbuzz():
    for k in range(1, 100):
        if (k % 5 == 0 and k % 3 == 0):
            print("FizzBuzz", end=" ")
        elif (k % 3 == 0):
            print("Fizz", end=" ")
        elif (k % 5 == 0):
            print("Buzz", end=" ")
        else:
            print(f"{k:d}", end=" ")
