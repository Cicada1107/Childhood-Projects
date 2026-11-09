#stack operation
#3

class Stack:
    """A stack in python."""
    def __init__(self): #Initialising the class object
        self.elements = []

    def isEmpty(self):
        """Returns True of the stack is empty. Returns False otherwise."""
        return len(self.elements) == 0

    def push(self, element):
        """Adds an element to the bottom of the stack"""
        self.elements.append(element)

    def pop(self):
        """Removes the top-most element of the stack"""
        self.elements.pop(0)

    def peek(self):
        """Returns the value of the top most element in the stack"""
        return self.elements[0]

    def size(self):
        """Returns the size of the stack"""
        return len(self.elements)

stack = Stack()#Creating a stack instance
print("Menu based Stack")
cd= True
while cd:
    print("1. Display", "2. Stack size", "3. Top-most value", "4. Push", "5. Pop", "6. Exit", sep = "\n")
    choice = int(input("Enter your choice: "))
    if choice == 1: print("The stack is: ", stack.elements)
    elif choice == 2: print("The size of the stack is: ", stack.size())
    elif choice == 3: print("The top-most value is: ", stack.peek())
    elif choice == 4: stack.push(int(input("Enter the element to insert: ")))
    elif choice == 5: stack.pop()
    elif choice == 6: break
    else: print("Invalid Choice!")     
