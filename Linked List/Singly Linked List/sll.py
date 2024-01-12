class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class SLL:
    def __init__(self):
        self.head = None

    def list_print(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

l = SLL()

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)

l.head = e1
l.head.next = e2
e2.next = e3

l.list_print()