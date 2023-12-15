class Queue:
    def __init__(self):
        self.queue_data = []
        self.first = -1
        self.last = -1
        self.is_queue_empty = self.first == -1

    def enqueue(self, value):
        if self.is_queue_empty:
            self.is_queue_empty = False
            self.first += 1
            
        self.last += 1
        self.queue_data.insert(self.last, value)

    def size(self):
        if self.is_queue_empty:
            return 0
    
        return len(self.queue_data)
    
    def dequeue(self):
        if self.is_queue_empty:
            return None

        element_to_return = self.queue_data[self.first]
        self.queue_data.pop(self.first)
        self.last -= 1

        if self.last == -1:
            self.first = -1
            self.last = -1
            self.is_queue_empty = True

        return element_to_return
        

    def __str__(self):
        if self.is_queue_empty:
            return "|\n| Empty\n|"
        
        queue_str = "|\n|"

        for element in self.queue_data:
            queue_str += f" <-({element})"

        queue_str += "\n|"

        return queue_str

        
