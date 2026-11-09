#Queue operations
#4

class Queue:
    """A queue in Python"""
    def __init__(self):     #Initializing the class
        self.elements = []

    def isEmpty(self):
        """Returns True if the queue is empty and False otherwise"""
        return len(self.elements) == 0

    def enqueue(self, item):
        """Enqueues a given item"""
        self.elements.append(item)

    def dequeue(self):
        """Dequeues an element"""
        return self.elements.pop(0)

    def peek(self):
        """Returns the value at the rear end of the queue"""
        return self.elements[-1]

    def size(self):
        """Returns the size of the queue"""
        return len(self.elements)

q = Queue()
print("Menu based queue".title())
cd = True
while True:
    print("1. Enqueue", "2. Dequeue", "3. Display", "4. Size of queue", "5. Value of rear", sep = '\n')
    choice = int(input("Enter a valid choice number: "))
    if choice == 1: q.enqueue(int(input("Enter the element to enqueue: ")))
    elif choice == 2:
        if q.isEmpty(): print("Queue is already empty")
        else: print("Dequeued the element: {}".format(q.dequeue()))
    elif choice == 3: print(q.elements)
    elif choice == 4: print("The size of the queue is: {}".format(q.size()))
    elif choice == 5: print("The value of rear element is: {}".format(q.peek()))
    else: print("Invalid choice")
