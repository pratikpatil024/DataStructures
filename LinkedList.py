# Node class
class Node(object):
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList(object):
    # Function to initialize LinkedList object
    def __init__(self):
        self.head = None
