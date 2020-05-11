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
    def __init__(self, name):
        self.stack = Stack()
        self.label = name

    def name(self):
        return self.label

    def isEmpty(self):
        return self.stack.isEmpty()

    def check(self, d):
        return self.stack.isEmpty() or d.get() < self.stack.peek().get()

    def peek(self):
        return self.stack.peek()

    def push(self, d):
        if self.check(d):
            self.stack.push(d)
            return True
        else:
            return False

    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return self.name() + "=>" + str(self.stack)

def moveOne(From, To):
    if To.check(From.peek()):
        d = From.pop()
        print ('Moving {} from {} to {}'.format(d, From.name(), To.name()))
        To.push(d)
        return True
    else:
        return False

fp = Pin('FP')
wp = Pin('WP')
tp = Pin('TP')

def setUp(n):
    for i in range(n, 0, -1):
        fp.push(Disk(i)) 
    print(fp)
    print('set up completed')
    print()
n = 2
setUp(n)

def logic(n):
    if n == 1:
        moveOne(fp, tp)
    if n == 2:
        moveOne(fp, wp)
        moveOne(fp, tp)
        moveOne(wp, tp)

    print()
    print(tp)

logic(n)