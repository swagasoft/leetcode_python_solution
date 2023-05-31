class Node:
    def __init__(self, data):
      self.name = data
      self.next = None
      self.next = None
      
      
class DoubleLinkedList:
    def __init__(self):
      self.head = None
      
    
    def is_empty(self):
        return self.head is None
    
    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            
    def insert_at_position(self, data):
        new_node = Node(data)                                     