from node import Node

class OrderedList():
    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        while current != None and item > current.getData():
            previous = current
            current = current.getNext()
        temp = Node(item)
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)
        temp.setNext(current)

    def remove(self, item):
        current = self.head
        previous = None
        while current != None and item > current.getData():
            previous, current = current, current.getNext()
        if current != None and current.getData() == item:
            if previous == None:
                self.head = None
            else:
                previous.setNext(current.getNext())
    
    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() < item:
                current = current.getNext()
            elif current.getData() == item:
                return True
            else:
                return False

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        counter = 0
        while current != None:
            counter += 1
            current = current.getNext()
        return counter

    def index(self, item):
        current = self.head
        index = 0
        while current != None:
            if current.getData() < item:
                current = current.getNext()
                index += 1
            elif current.getData() == item:
                return index
            else:
                break
        return -1

    def pop(self, pos = 0):
        current = self.head
        previous = None
        index = 0
        while current != None:
            if index < pos:
                previous, current = current, current.getNext()
                index += 1
            elif index == pos:
                if previous == None:
                    temp = self.head
                    self.head = temp.getNext()
                    return temp.getData()
                else:
                    previous.setNext(current.getNext())
                    return current.getData()
            else:
                raise Exception("element not found at pos")

    # def pop(self):
    #     if self.head == None:
    #         raise Exception()
    #     else:
    #         temp = self.head
    #         self.head = self.head.getNext()
    #         return temp
    def __str__(self):
        current = self.head
        data = []
        while current != None:
            data.append(current.getData())
            current = current.getNext()
        return str(data)


mylist = OrderedList()
# print(mylist.isEmpty())
# print(mylist.size())
# print(mylist)
# print(mylist.pop(10))

mylist.add(4)
mylist.add(10)
mylist.add(2)
print(mylist)
print(mylist.index(11))
# mylist.remove(4)
print(mylist.pop(3))
print(mylist)
