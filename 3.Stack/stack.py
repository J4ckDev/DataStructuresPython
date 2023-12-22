class Stack:

    def __init__(self):
        self.stack_data = []
        self.is_stack_empty = True

    def size(self):
        return len(self.stack_data)

    def push(self, value):
        self.stack_data.append(value)
        self.is_stack_empty = False

    def pop(self):
        if self.is_stack_empty:
            return None
        
        element_to_return = self.stack_data.pop()

        is_stack_empty_now = self.size() == 0
        if is_stack_empty_now:
            self.is_stack_empty = True

        return element_to_return
    
    def __str__(self):
        if self.is_stack_empty:
            return "Empty"
        
        stack_str = "\n"
        
        total_elements = self.size()

        for index in range(total_elements - 1, -1, -1):
            is_first_element = index == total_elements - 1
            if is_first_element:
                stack_str += f"|__{self.stack_data[index]}\n"
                continue
            stack_str += f"|__{self.stack_data[index]}\n"
                        
        return stack_str
            
        
        