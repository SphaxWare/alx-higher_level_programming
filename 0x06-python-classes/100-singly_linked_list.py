#!/usr/bin/python3
class Node:
    """
    Node class represents a node in a singly linked list.

    Attributes:
    - data (int): The data stored in the node.
    - next_node (Node): Reference to the next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node.

        Parameters:
        - data (int): The data to be stored in the node.
        - next_node (Node): Reference to the next node in the linked list.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data attribute.

        Returns:
        int: The data stored in the node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.

        Parameters:
        - value (int): The new value for the data attribute.

        Raises:
        - TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.

        Returns:
        Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.

        Parameters:
        - value (Node): The new value for the next_node attribute.

        Raises:
        - TypeError: If the provided value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class represents a singly linked list.

    Attributes:
    - head (Node): The first node in the linked list.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct sorted position in the list.

        Parameters:
        - value (int): The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
        str: String representation of the linked list.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data)
            current = current.next_node
            if current:
                result += "\n"
        return result
