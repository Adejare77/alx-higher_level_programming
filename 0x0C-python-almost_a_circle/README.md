#!/usr/bin/bash

0x0C. Python - Almost a circle

This Project Creates a Base Model, from which Rectangular Model and Square Model inherits.
The rectangular Model inherits from the Base Model, while the Square Model inherits from the Rectangle Model.

Basically, the idea is about creating a rectangle and square and saving them into a file using JSON format. It also gives the position where the rectangle and square can be located in a 2D-plane.

The methods defined in the Base Model are as follows:
1.to_json_string
2. save_to_file
3. from_json_string
4. create
5. load_from_file

The methods defined in the Rectangle Model after inheriting from the Base Model include:
1. validator
2. width
3. height
4. x
5. y
6. area
7. display
8. update
9. to_dictionary

The methods defined in the Square Model after inheriting from the Rectangle Model include:
1. size
2. update
3. to_dictionary
