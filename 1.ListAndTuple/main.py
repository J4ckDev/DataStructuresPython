list_of_integers = [7, 5, 2, 9, 30, 100, 70]
list_of_strings = ["apple", "banana", "cherry"]
list_of_floats = [1.1, 2.2, 3.3, 4.4, 5.5]
list_of_mixed = [1, "apple", 3.4, True, "mango", 5.5]

print(list_of_integers[3]) # retorna 9
print(list_of_strings[1]) # retorna banana
print(list_of_floats[2]) # retorna 3.3
print(list_of_mixed[4]) # retorna mango

print(list_of_integers.sort()) 
print(list_of_strings.reverse())
list_of_floats.append(6.6)
print(list_of_floats)
list_of_mixed.insert(2, False)
print(list_of_mixed)
list_of_floats.remove(2.2)
print(list_of_floats)
list_of_strings.extend("orange")
print(list_of_strings)
list_of_strings.clear()
print(list_of_strings)
print(list_of_integers.__contains__(7))

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][1]) # retorna 5
print(nested_list[2][0]) # retorna 7


tuple_of_integers = (7, 5, 2, 9, 30, 100, 70)
print(tuple_of_integers[3]) # retorna 9
