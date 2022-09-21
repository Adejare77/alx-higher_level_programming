#!/usr/bin/python3
x = 97
while x <= 122:
	if (chr(x) != 'q' and chr(x) != 'e'):
		print(f"{chr(x)}", end="")
	x += 1
