#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ Defines a Student """
    def __init__(self, first_name, last_name, age):
        """ Instantiation of the first, last and age of the student

            Args:
                first_name: first name of the student
                last_name: last name of the student
                age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a student """
        return self.__dict__
