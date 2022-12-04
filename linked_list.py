class Node:
    """
        An object to storing a single node of a linked list
        Models two attribute - data and link to the next node in the list 
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
        Singly linked list 
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
         Returns the number of nodes in the list
         Tackes o(n) time 
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds new Node Containing data at the ende of the list
        Takes o(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
             Search for the first Node containing which matches the given key
             Return the node or None if not found 
             Takes o(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data,  index):
        """
        Inserts a New Node containing data at index position
        Insert takes o(1) time but finding a node at insertion position takes o(n) time
        overall it takes o(n) time 
        """
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index 
            current = self.head
            while position > 1:
                current= node.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new 
            new.next_node = next_node

    def __repr__(self):
        """
          return string representaion of the List
          Takes O(n) time  
        """
        node = []
        current = self.head
        while current:
            if current is self.head:
                node.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                node.append("[Tail: %s]" % current.data) 
            else:
                node.append("[%s]" % current.data)
            current = current.next_node

        return '-> '.join(node)
