#!/usr/bin/python3
import dis, calculator_1
def magic_calculation(a, b):
    print(dis.dis(calculator_1.add))
    print(dis.dis(calculator_1.sub))
    print(dis.dis(calculator_1.mul))
    print(dis.dis(calculator_1.div))
magic_calculation(3, 4)
