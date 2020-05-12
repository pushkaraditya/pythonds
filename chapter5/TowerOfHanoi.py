import sys
sys.path.append('..')

from basic.stack import Stack

class Globals():
    moveNumber = 0

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
        Globals.moveNumber = Globals.moveNumber + 1
        print ('{}. Moving {} from {} to {}'.format(Globals.moveNumber, d, From.name(), To.name()))
        To.push(d)
        return True
    else:
        return False

A = Pin('Pin A')
B = Pin('Pin B')
C = Pin('Pin C')
pins = [A,B,C]

def setUp(fp, n):
    for i in range(n, 0, -1):
        fp.push(Disk(i)) 
    print(fp)
    print('set up completed. {0} has {1} disks'.format(fp.name(), n))
    print()

def calculateWP(pins, fp, tp):
    tmp = [p for p in pins]
    tmp.remove(fp)
    tmp.remove(tp)
    return tmp[0]

def logic(pins, fp, tp, n):
    if n == 1:
        moveOne(fp, tp)
        return 1
    else:
        wp = calculateWP(pins, fp, tp)
        moves = logic(pins, fp, wp, n - 1)
        moveOne(fp, tp)
        moves += logic(pins, wp, tp, n - 1)
        return moves + 1


n = 16
setUp(A, n)

moves = logic(pins, A, C, n)
print()
print('it has taken {0} moves'.format(moves))
print(C)
