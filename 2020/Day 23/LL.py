class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.prev = self

    def __repr__(self):
        return self.data

class LinkedList:
    def appendleft(self, node):
        if not self.head:
            self.head = node
            return
        node.prev = self.head.prev
        node.next = self.head
        self.head.prev.next = node
        self.head.prev = node
        self.head = node
        
    def append(self, node):
        if not self.head:
            self.head = node
            return
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
        
    def add3after(self, target_node_data, new_node1, new_node2, new_node3):
        if not self.head:
            raise Exception("List is empty")
        for node in self:
            if node.data == target_node_data:
                new_node1.next = new_node2
                new_node2.next = new_node3
                new_node3.next = node.next
                new_node1.prev = node
                new_node2.prev = new_node1
                new_node3.prev = new_node2
                node.next.prev = new_node3               
                node.next = new_node1
                return
        raise Exception("Node with data '%s' not found" % target_node_data)

    def rotate(self, n):
        node = self.head
        if n>0:
            for _ in range(n):
                node = node.next 
        elif n<0:
            for _ in range(-n):
                node = node.prev
        self.head = node    

    def popleft(self):
        node = self.head.data
        self.head.next.prev = self.head.prev
        self.head.prev.next = self.head.next
        self.head = self.head.next
        return node

    def __init__(self, values = None):
        if type(values) is not list:
            self.head = None
        else:
            nodes = []
            for value in values:
                nodes.append(Node(value))
            self.head = nodes[0]
            for i,node in enumerate(nodes[:-1]):
                node.next = nodes[i+1]
                node.prev = nodes[i-1]
            nodes[-1].next = self.head
            nodes[-1].prev = nodes[-2]
            
                

    def __repr__(self):
        node = self.head
        nodes = []
        nodes.append(str(node.data))
        node = node.next
        while node is not self.head:
            nodes.append(str(node.data))
            node = node.next
            
        # nodes.append("None")
        return ', '.join(nodes)

    def __iter__(self):
        node = self.head
        yield node
        node = node.next
        while node is not self.head:
            yield node
            node = node.next
            
    

            
