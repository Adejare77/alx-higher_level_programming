#!/usr/bin/python3
""" Creating a Circle """

import json
import csv


class Base:
    """Base of the Circle"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """if id is not None, assigns the public instance attribute id
            with id value - you can assubme id is an integer.
            otherwise, increment __nb_objects and assign the new value
            to the public instance attribute id

        Args:
            id (int, optional): unique identification for each given instances.
                Defaults to None.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """returns the JSON string representation of list_dictionaries

        Return:
            if list_dictionaries is None or empty, return the string:
            "[]"
            Otherwise, return the JSON string representation of
            list_dictionaries
        """
        if not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs
            to a file

        Args:
            list_objs (list): list of instances who inherits of Base.
                e.g: list of Rectangle or list of Square instances

        Description:
            if list_objs is None, save an empty list
            The filename must be: <Class name>.json - example: Rectangle.json
            Must overwrite the file it it already exists
            Must use the static method "to_json_string"
        """
        file_name = cls.__name__ + ".json"
        if not list_objs:
            list_objs = []
        dict_repr = [obj.to_dictionary() for obj in list_objs]
        json_repr = cls.to_json_string(dict_repr)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(json_repr)

    @staticmethod
    def from_json_string(json_string) -> list:
        """returns the list of JSON string representation json_string:

        Args:
            json_string (list): is a string representating a list of
            dictionaries

        Returns:
            list: if json_string is None or empty, return an empty list,
            otherwise, return the list represented by json_string
        """
        if not json_string:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.

        Args:
            dictionary (dict): dictionaries of key/values to be updated

        Description:
            Unlike using instance method, which requires an instance,
            class method can be called without creating an instance
            (e.g Rectangle.create()). Class method takes all instance methods
            including __init__() but doesn't require an instance to be created.
            For RECTANGLE, it requires 5 parameters, 3 of which have a default
            values (x, y, id). This means that parameters "width and height"
            need to be given.

            Also, for SQUARE, it requires 4 parameters, 3 of which are also
            given defaults (x, y, id). This means that the parameter "size"
            needs to be given.

            Note: we are required to Rectangle or Square instance with 'dummy'
            mandatory attributes(width, height, size, etc). This is of course
            needed because we'll just be given a dictionary data to update
            (check example). This dummy is an instance of a class that will
            be overidden by dictionary we supplied. since, cls inherits all
            methods, we need to give the required parameters for width,
            height and size in Rectangle and Square classes for dummy.
            This dummies are what we will update when we need it.
        """
        if cls.__name__ == "Rectangle":
            """
            Creating a dummy rectangle instance with "height and width"
            set as 7, 8 respectively. This could be any number, since it really
            has no effect. That is, they follow the argument given by the
            instance and not by the class. W and H must be > 0
            """
            dummy = cls(8, 7)  # We now have a dummy that we can update anytime
            dummy.update(**dictionary)  # The instance dummy can now be updated
            return dummy

        elif cls.__name__ == "Square":
            """
            This is same as that of Rectangle. However, the only missing
            parameter here is the size. Thus, cls(a) gives size
            """
            dummy = cls(12)  # A dummy for Square class that we can update
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls) -> list:
        """returns a list of instances

        Description:
            filename must be: <Class name>.json - e.g: Rectangle.json
            if file doesn't exist, return an empty list, otherwise, return
            a list of instances - the type of these instances depends on
            cls (current class using this method)
            must use the from_json_string() and create() methods
        Returns:
            list: contains list of all instances created
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as f:
                file = f.read()
            dict_repr = cls.from_json_string(file)
            instances = [cls.create(**obj) for obj in dict_repr]
        except FileExistsError:
            instances = []
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs) -> None:
        """serializes in CSV

        Args:
            list_objs (list): list of instances to be saved
        """
        file_name = cls.__name__ + ".csv"
        if not list_objs:
            list_objs = []
        else:
            dict_repr = [obj.to_dictionary() for obj in list_objs]
            with open(file_name, "w", encoding="utf-8") as csv_file:
                fieldnames = [x for x in dict_repr[0]]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(dict_repr)

    @classmethod
    def load_from_file_csv(cls) -> list:
        """Deserializes csv / load from a csv file

        Returns:
            list: contains list of all instances created
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline='', encoding="utf-8") as csv_fil:
                csv_reader = csv.DictReader(csv_fil, delimiter=",")
                dict_list = [{k: int(v) for k, v in instance.items()}
                             for instance in csv_reader]
                instances = [cls.create(**obj) for obj in dict_list]
        except FileExistsError:
            instances = []
        return instances
