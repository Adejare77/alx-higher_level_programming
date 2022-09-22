#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as names
    for name in names:
        if (name[:2] != '__'):
            print(name)
