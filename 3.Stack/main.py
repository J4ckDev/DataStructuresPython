from stack import Stack

stack_obj = Stack()
stack_obj.push(1)
stack_obj.push('Hola mundo')
stack_obj.push(7)
stack_obj.push(122)
print(stack_obj)
stack_obj.pop()
print(stack_obj)
stack_obj.push('otro item')
print(stack_obj)
