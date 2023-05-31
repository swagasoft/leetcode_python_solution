

class Node:
    def __init__(self, value):
      self.value = value
      self.next = None


class SingleLinkedList:
  
  def __init__(self):
     self.head = None
  
  
  
  def is_empty(self):
    return self.head is None
  
  
  
  def display(self):
    if self.is_empty():
      print("Linked list is Empty")
      return
    
    current = self.head
    while current:
      print('[{}]'.format(current.value))
      current = current.next
    
     
  
  def add_to_tail(self, value):
    new_Node = Node(value)
    if self.head == None:
      print("Linked list is empty, the new Node is now the head.")
      self.head  = new_Node
      return
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_Node
     
  
   
  def add_to_head(self, value):
      new_node = Node(value)
      new_node.next = self.head
      self.head =  new_node
      
      
      
  def insert_after_value(self, target_value, new_value):
    new_Node = Node(new_value)
    current =  self.head
    while current:
      if current.value == target_value:
        new_Node.next = current.next
        current.next = new_Node
        break
      current =  current.next
      
      
      
  def delete(self, target_value):
    if self.is_empty():
      print('Cannot delete cos list is empty!')
      return False
    
    if (self.head.value == target_value):
      self.head = self.head.next
      return True
    
    current = self.head
    while current.next:
      if current.next.value == target_value :
        current.next = current.next.next
        break
      current =  current.next
      
      


single_linked_list = SingleLinkedList()
single_linked_list.add_to_tail(1)
single_linked_list.add_to_tail(2)
single_linked_list.add_to_tail(3)
single_linked_list.add_to_tail(4)
single_linked_list.add_to_tail(5)
single_linked_list.add_to_tail(6)
single_linked_list.add_to_head(9)
single_linked_list.insert_after_value(2,22)
print('Is empty ', single_linked_list.is_empty())
print(single_linked_list.display())
single_linked_list.delete(1)
print("----------------------------")
print(single_linked_list.display())

      