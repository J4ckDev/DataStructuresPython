from queue import Queue

queue_obj = Queue()
queue_obj.enqueue(1)
print(queue_obj)
queue_obj.enqueue(2)
print(queue_obj)
queue_obj.enqueue(3)
print(queue_obj)
print(queue_obj.dequeue())
print(queue_obj)