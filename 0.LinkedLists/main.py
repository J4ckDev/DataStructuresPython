from linked_list import LinkedList

linked_list_obj = LinkedList()
linked_list_obj.insert(1)
linked_list_obj.insert('Hola')
linked_list_obj.insert(True)
linked_list_obj.insert(4)
linked_list_obj.insert(5)
linked_list_obj.insert(5)
linked_list_obj.insert(None)
print(linked_list_obj)
print(linked_list_obj.length())
linked_list_obj.remove(5)
linked_list_obj.remove(5)
print(linked_list_obj)
print(linked_list_obj.length())