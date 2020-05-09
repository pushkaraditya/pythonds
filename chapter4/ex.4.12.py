import sys
sys.path.append('../')

from basic.queue import Queue

q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print(q.dequeue())