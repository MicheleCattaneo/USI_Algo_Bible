class Node:
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev

class EndOfStack():
    pass

class Stack:
    def __init__(self):
        self.size = 0
        self.top = EndOfStack()

    def isEmpty(self):
        return isinstance(self.top, EndOfStack)

    def add(self, value):
        new = Node(value, self.top)
        self.top = new

    def pop(self):
        if isinstance(self.top, EndOfStack):
            return "End of stack"

        temp = self.top.value
        self.top = self.top.prev
        return  temp

    def print(self):
        curr = self.top
        while isinstance(curr, Node):
            print(curr.value)
            print("__")
            curr = curr.prev



stack = Stack()
print(stack.isEmpty())
stack.add(3)
stack.add(4)
stack.add(9)
stack.add(7)
#stack.print()

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
