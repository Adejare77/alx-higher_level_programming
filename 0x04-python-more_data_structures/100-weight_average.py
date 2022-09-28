#!/usr/bin/python3
""" function that returns the weighted average of all integer tuple """


def weight_average(my_list=[]):
    score = [(i * k) for i, k in my_list]
    weight = [i[1] for i in my_list]
    result = sum(score) / sum(weight)
    return result
