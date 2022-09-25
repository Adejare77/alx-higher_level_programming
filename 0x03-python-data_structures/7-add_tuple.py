#!/usr/bin/python3
""" function that adds 2 tuples """

def add_tuple(tuple_a=(), tuple_b=()):
    """ adds two argument

        Args:
            tuple_a: first argument
            tuple_b: second argument
        Returns:
            tuple with 2 integers
    """
    a = []
    b = []
    for i in tuple_a:
        a.append(i)
    for k in tuple_b:
        b.append(k)
    if (len(a) < 2 or len(b) < 2):
        while (len(a) < 2):
            a.append(0)
        while (len(b) < 2):
            b.append(0)
    return (a[0] + b[0], a[1] + b[1])
            
        
        
