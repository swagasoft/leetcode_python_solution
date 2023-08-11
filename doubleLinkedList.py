class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
      
      
class DoubleLinkedList:
    def __init__(self):
      self.head = None
      
    
    def is_empty(self):
        return self.head is None
    
    def display(self):
        if(self.is_empty()):
            return print("Linked is Empty")
        current_node = self.head
        while (current_node):
            print("[{}]".format(current_node.data))
            current_node = current_node.next
    
    
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
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node
            
            
    def insert_at_position(self,position, data):
        if position <= 0:
            self.insert_at_head(data)
        else:
            new_Node = Node(data)
            current_node = self.head
            count = 0
            while current_node is not None:
                if count == position:
                # insert at the position
                    new_Node.next = current_node
                    new_Node.prev = current_node.prev
                    current_node.prev.next = new_Node
                    current_node.prev = new_Node
                    return True
                    
                current_node = current_node.next #Keep on looping
                count += 1
            print("Position out of bounds")
            return False
        
            
    def remove_from_head(self):
        if(self.is_empty()):
            print("Linked is empty")
            return False
        elif self.head.next is None:
            #ONly one Node in the list
            self.head = None
            return True
        else:
            self.head = self.head.next
            self.head.prev = None
            return True
            
            
    def remove_from_tail(self):
        if(self.is_empty()):
            print("List ")
            return False
        if self.head.next is None:
            # only one node in the list
            self.head = None
            return True
        
        current_node =  self.head
        while current_node.next:
            if current_node.next.next is None:
                current_node.next = None
                return True
            current_node = current_node.next
            
            
    def search(self, value):
        if(self.is_empty()):
            return False
        index = 0
        current = self.head
        
        while (current.data != value):
            if current.data == value:
                return index
            current = current.next
            index += 1
            if current is None:
                return False
        return index
            
            
                                              
                                              
doubleLink = DoubleLinkedList()
doubleLink.insert_at_head(1)
doubleLink.insert_at_head(2)
doubleLink.insert_at_head(3)
doubleLink.insert_at_tail(23)
doubleLink.insert_at_position(3,222)
doubleLink.remove_from_head()
print("Found ", doubleLink.search(0))
print("ls ", doubleLink.display())

