from node import Node

class LinkedList:
    def __init__(self):
        self.__start = None
        self.__length = 0
    
    def length(self):
        return self.__length

    def insert(self, value):
        if self.__start == None:
            self.__start = Node(value)
            self.__length = 1
        else:
            current_node = self.__start
            while current_node.next() is not None:
                current_node = current_node.next()
            current_node.next(Node(value))
            self.__length += 1

    def render_node(self, value):
        return f"|{value}|-> "

    # Eliminar y retornar el primer nodo
    def shift(self):
        node_to_return = None
        if self.__start is not None:
            node_to_return = self.__start
            self.__start = node_to_return.next()
            self.__length -= 1
            node_to_return.next(None)
        return node_to_return

    # Eliminar y retornar el último nodo
    def pop(self):
        last_node = None
        current_node = self.__start
        while current_node is not None:
            next_node = current_node.next()
            if next_node is not None:
                last_node = current_node
                current_node = next_node
            else:
                break
        
        if last_node == None:
            self.__start = None
            self.__length = 0
        else:
            last_node.next(None)
            self.__length -= 1

        return current_node

    # Eliminar y retornar el primer nodo que contenga el valor especificado
    def remove(self, value):
        last_node = None
        current_node = self.__start
        while current_node is not None:
            next_node = current_node.next()
            current_value = current_node.value()
            if current_value == value and type(current_value) == type(value):
                if last_node is not None:
                    last_node.next(next_node)
                else:
                    self.__start = next_node

                self.__length -= 1
                current_node.next(None)
                return current_node
            else:
                last_node = current_node
                current_node = next_node
        return None


    # Traversing a Linked List
    def __str__(self):
        if self.__start == None:
            return 'empty'

        current_node = self.__start
        nodes_rendered = ''
        while current_node is not None:
            nodes_rendered += self.render_node(current_node.value())
            current_node = current_node.next()

        return nodes_rendered + "null"
