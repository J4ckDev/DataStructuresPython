class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def value(self) -> any:
        return self.__value

    def next(self, node=False):
        if isinstance(node, Node) or node == None:
            self.__next = node
        return self.__next

    def __str__(self):
        return f"|{self.__value}|-> {self.__next}"