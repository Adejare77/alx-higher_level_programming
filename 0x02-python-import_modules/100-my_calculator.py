#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as func
    import sys
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        list_ = [('+', func.add(a, b)), ('-', func.sub(a, b)),
                 ('/', func.div(a, b)), ('*', func.mul(a, b))]
        operators = list('+-/*')
        if sys.argv[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            for i, v in list_:
                if sys.argv[2] == i:
                    print("{} {} {} = {}".format(a, i, b, v))
