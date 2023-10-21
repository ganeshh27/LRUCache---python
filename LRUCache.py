
#implement lru using dictionary and doublylinked list
#dictionary is used to get the value at O(1) time 
#doubly linked list is used to add/remove/update the key based on LRU.(tried using deque, but reordering list takes O(n) time)


class DoublyListNode: 
    def __init__(self, key, value): 
        self.value = value
        self.key = key 
        self.prev = None
        self.next = None
 
class LRUCache: 
  
    def __init__(self, capacity=20): 
        # capacity:  capacity of cache 
        # Initialize all variable 
        self.capacity = capacity 
        self.map = {} 
        self.head = DoublyListNode(0, 0) 
        self.tail = DoublyListNode(0, 0) 
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.count = 0
  
    def deleteNode(self, node): 
        node.prev.next = node.next
        node.next.prev = node.prev 
  
    def addToHead(self, node): 
        node.next = self.head.next
        node.next.prev = node 
        node.prev = self.head 
        self.head.next = node 
  
  
    def refer(self, key): 
        if key in self.map: 
            node = self.map[key] 
            self.deleteNode(node) 
            self.addToHead(node) 
            print('key: ', key, "value: ", node.value)
            return node.value 
        print('key: ', key,  ' not found')
        return -1
  
    # This method works in O(1) 
    def add(self, key, value): 
        
        if key in self.map: 
            node = self.map[key] 
            node.value = value 
            self.deleteNode(node) 
            print('key: ', key, ' added')
            self.addToHead(node) 
        else: 
            node = DoublyListNode(key, value) 
            self.map[key] = node 
            if self.count < self.capacity: 
                self.count += 1
                print('key: ', key, ' added')
                self.addToHead(node) 
            else: 
                #delete last(right most/least recently used)
                del self.map[self.tail.prev.key] 
                self.deleteNode(self.tail.prev) 
                print('key: ', key, ' added')
                self.addToHead(node) 
  
if __name__ == '__main__': 
  laptopcache=LRUCache(3)
  laptopcache.add(1, 'hp');
  laptopcache.refer(1)
  laptopcache.add(2,'dell');
  laptopcache.add(3,'asus');  
  laptopcache.refer(2)
  laptopcache.refer(1)
  laptopcache.add(4, 'acer')
  laptopcache.refer(3)
  laptopcache.refer(1)
