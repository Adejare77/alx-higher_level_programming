#!/usr/bin/pthon3
""" Singly linked list """

class Node:
    """ defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """ instantiation of data and next_node """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not (next_node == None or next_node == Node):
            self.__next_node = next_node

    # getting data values
    @property
    def data(self):
        """ retrieves new data """
        return self.__data

    # setting data values
    @data.setter
    def data(self, value):
        """ sets new data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    # getting next_node values
    @property
    def next_node(self):
        """ retrieves new next_node """
        return self.current.next_node

    # setting next_node values
    @next_node.setter
    def next_node(self, value):
        """ sets the next_node """
        new_node = SinglyLikedList()
        if not new_node.head:
            new_node.head = Node(value)
        else:
            current = new_node.head
            while current.next_node:
                current = current.next_node
            current.next_node = Node(value)

class SinglyLinkedList:
    """ add node """
    def __init__(self):
        self.head = None
    
    def sorted_insert(self, value):
        """ inserts node using value to determine the right position """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
    def printable(self):
        _print = self.head
        while _print:
            print(_print.data)

