

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
# 使用栈对字符串"yesterday"进行逆序
stack=Stack()
for c in "yesterday":
    stack.push(c)
reverse = ""
for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)

# 使用栈创建一个新列表，将如下列表中的元素逆序排列：[1, 2, 3, 4, 5]。
list1 = [1, 2, 3, 4, 5]
list2 = []
stack=Stack()
for c in list1:
    stack.push(c)

for i in range(len(stack.items)):
    list2.append(stack.pop())

print(list2)