import sys
sys.path.append('..')

from basic.stack import Stack

class Disk():
    def __init__(self, size):
        self.size = size

    def get(self):
        return self.size
    
    def __str__(self):
        return str(self.size)


class Pin():
    def __init__(self):
        self.stack = Stack()

    def isEmpty(self):
        return self.stack.isEmpty()

    def check(self, d):
        return self.stack.isEmpty() or d.get() < self.stack.peek().get()

    def push(self, d):
        if self.check(d):
            self.stack.push(d)
            return True
        else:
            return False

    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)


# pin = Pin()
# pin.push(Disk(2))
# # print(pin)
# pin.push(Disk(1))
# print(pin)
# print(pin.push(Disk(13)))
# print(pin)
