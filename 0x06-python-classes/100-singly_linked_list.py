#!/usr/bin/python3
""" This module defines a node of a singly linked list. """


class Node:
    """Node of a singly linked list.
    Private instance attribute: data:
        - property def data(self)
        - property setter def data(self, value)
    Private instance attribute: next_node:
        - property def next_node(self)
        - property setter def next_node(self, value)
    Instantiation with data and next_node.
    """

    def __init__(self, data, next_node=None):
        """Initializes the data of the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data from the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data into a node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Singly linked list.
    Private instance attribute: head.
    Simple instantiation.
    Public instance method: def sorted_insert(self, value).
    """

    def __init__(self):
        """Initializes the linked list."""
        self.head = None

    def __str__(self):
        """For the print statement in the main file."""
        my_str = ""
        node = self.head
        while node:
            my_str += str(node.data)
            my_str += '\n'
            node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
