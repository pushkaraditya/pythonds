from node import Node

class UnorderedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        cn = self.head # current node
        counter = 0
        while cn != None:
            cn = cn.getNext()
            counter += 1
        return counter

    def search(self, item):
        cn = self.head
        while cn != None:
            if cn.getData() == item:
                return True
            cn = cn.getNext()
        return False

    def remove(self, item):
        cn = self.head
        previous = None
        while cn != None:
            if cn.getData() == item:
                if previous == None:
                    self.head = self.head.getNext()
                else:
                    previous.setNext(cn.getNext())                
                return
            previous = cn
            cn = cn.getNext()
        return False

    def __str__(self):
        current = self.head
        data = []
        while current != None:
            data.append(current.getData())
            current = current.getNext()
        return str(data)


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist.size())

# print(mylist.search(26))
# print(mylist.search(27))
mylist.remove(31)
print(mylist.size())
