
class Node:
    def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      
      
      
class BinarySearchTree:
    def __init__(self):
      self.root = None
      
      
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(key, self.root)
        
        
    def _insert_recursive(self, key: int, node : Node):
        if key  < node.key:
            if node.left  is None:
                node.left = Node(key)
            else:
                self._insert_recursive(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(key, node.right)
    
    def search(self, key):
        return self._search_recursive(key, self.root)
                
    
    def _search_recursive(self, key: int, node: Node):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(key, node.left)
        return self._search_recursive(key, node.right)
    
    def _delete_recursive(self,key: int, node: Node):
        if node is None:
            return node
        
        if key < node.left:
            node.left = self._delete_recursive(key,node.left)
        elif key >  node.key:
            node.right = self._delete_recursive(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.key = successor.key
                node.right =    self._delete_recursive(successor.key, node.right)
        return node
                
    def _find_min(self: int, node: Node):
        current = node
        while current.left is None:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node is not None:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.key)
            self._inorder_traversal_recursive(node.right, result)
    

bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)
# print("BST ", bst)
print("BST_travers ", bst.inorder_traversal())