
class Node:

    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev, self.next = None



class LRCCache:
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}  # map key to node
        #left=LRU, right=most recent
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
        # remove node from list
    @classmethod
    def remove(self, removingNode):
        prev, next = removingNode.prev, removingNode.next
        prev.next, next.prev = next, prev

    # inert node at right
    @classmethod
    def insert(self, newNode):
        prev, next = self.right.prev, self.right
        prev.next, next.prev = newNode
        newNode.next , newNode.prev = next, prev


    @classmethod
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    @classmethod
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            leastUsedNode = self.left.next
            self.remove(leastUsedNode)
            del self.cache[leastUsedNode.keys]



lruMain = LRCCache(5)
lruMain.put(1,10)
lruMain.put(2,20)
lruMain.put(3,30)
print('ls ', lruMain)
