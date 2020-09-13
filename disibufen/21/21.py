class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.is_empty())

stack.push(1)
print(stack.is_empty())

item = stack.pop()
print(item)
print(stack.is_empty())

# for i in range(0, 10):
#     stack.push(i)
#
# print(stack.peek())
# print(stack.size())

for c in "Hello":
    stack.push(c)

reverse = ""

for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)




class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


e_queue=Queue()
print(e_queue.is_empty())

for i in range(0,5):
    e_queue.enqueue(i)

print(e_queue.size())

for i in range(5):
    print(e_queue.dequeue())

print()
print(e_queue.size())