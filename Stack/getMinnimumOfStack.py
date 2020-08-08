
# Design a stack that supports getMin() in O(1) time and O(1) extra space
class Stack():
    def __init__(self):
        self.items = []
        self.min = None

    def push(self, item):
        self.items.append(item)
        self.minimum()

    def pop(self):
        if self.isEmpty():
            raise ValueError('Empty stack')
        else:
            return self.items.pop()

    def minimum(self):
        if self.min is None:
            self.min = self.peek()
        else:
            if self.peek() < self.min:
                self.min = self.peek()

    def getMinimum(self):
        return self.min

    def peek(self):
        try:
            return self.items[-1]
        except IndexError as e:
            print(e)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

stack = Stack()

nums = [6,4,8,9,5,2,3]
for i in nums:
    stack.push(i)

print(stack.getMinimum())

HMSAAc%@%283