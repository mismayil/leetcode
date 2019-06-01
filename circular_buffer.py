class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.elems = [None for _ in range(size)]
        self.front = self.rear = -1

    def front(self):
        return self.elems[self.front]

    def rear(self):
        return self.elems[self.rear]

    def enqueue(self, elem):
        isfull = (self.rear == self.size - 1) & (self.front == 0) | (self.rear == self.front - 1)

        if isfull: return print('Queue is Full')

        self.rear = (self.rear + 1) % self.size
        self.elems[self.rear] = elem
        self.front = self.front if self.front != -1 else 0

    def dequeue(self):
        if self.front == -1: return print('Queue is Empty')

        elem = self.elems[self.front]

        if self.front + 1 > self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return elem

    def display(self):
        if self.front == -1:
            print ("Queue is Empty")

        elif self.rear >= self.front:
            print("Elements in the circular queue are:", end = " ")
            for i in range(self.front, self.rear + 1):
                print(self.elems[i], end = " ")
            print ()

        else:
            print("Elements in Circular Queue are:", end = " ")
            for i in range(self.front, self.size):
                print(self.elems[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.elems[i], end = " ")
            print()

        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")

ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print ("Deleted value = ", ob.dequeue())
print ("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
ob.enqueue(6)
