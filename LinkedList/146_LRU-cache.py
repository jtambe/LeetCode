"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.

There are two ambiguities in the task description. Please clarify the description, because taking the intention from the failed test cases is unnecessarily cumbersome.

a) The description does not specify which operations count as "use", i.e. which operation should trigger an LRU status update. get and set both do, and the description should say so.

b) The wording for set() can suggest set-only-upon-add behaviour. Consider reading: "((Set or insert) if the key is not present)". Please change to something along: "Set key, or add it if not present".
"""


class Node:
    """
    class to represent doubly linked list node
    """
    def __init__(self, key: int, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.lru_dll_head = None
        self.lru_dll_tail = None
        self.lru_store = {}
        self.lru_store_limit = capacity

    def _print_dll_keys(self):
        """
        debugger function to print doubly linked list
        """
        cur = self.lru_dll_head
        while cur:
            # print(f"key: {cur.val}")
            cur = cur.next

    def _search_dll(self, key:int) -> None:
        """
        1. Search if the key exists in DLL.
        2. If it exists, find the node for that key in doubly linked list
        3. If the node is middle of the DLL, change the next and prev node configurations and move the matching node to tail
        4. If the node is head, change the configurations and move the head to tail
        5. if the node is tail, don't need any operation

        """
        # find the node with key
        cur = self.lru_dll_head
        while cur and cur.key != key:
            cur = cur.next
        
        # if node is found
        if cur and cur is not self.lru_dll_head and cur is not self.lru_dll_tail :
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            # move the node to the tail
            self.lru_dll_tail.next = cur
            cur.prev = self.lru_dll_tail
            cur.next = None
            self.lru_dll_tail = cur
        elif cur and cur is self.lru_dll_head and cur is not self.lru_dll_tail:
            # head changes
            head = self.lru_dll_head
            self.lru_dll_head = self.lru_dll_head.next
            self.lru_dll_head.prev = None
            # tail changes
            self.lru_dll_tail.next = head
            head.prev = self.lru_dll_tail
            self.lru_dll_tail = head
            self.lru_dll_tail.next = None




    def _add_tail(self, key:int) -> None:
        """
        Refactored adding a key to the tail as separate function since it is being repeated.
        """
        if self.lru_dll_head is None:
            self.lru_dll_head = self.lru_dll_tail = Node(key)
        else:
            newNode = Node(key)
            self.lru_dll_tail.next = newNode
            newNode.prev = self.lru_dll_tail
            self.lru_dll_tail = newNode


    def get(self, key: int) -> int:
        """
        returns the value of key in LRU cache if exists else returns -1
        """
        # print(f"get request for key:{key}")
        if key in self.lru_store:
            self._search_dll(key)
        # self._print_dll_keys()
        return self.lru_store.get(key, -1)
        
    def put(self, key: int, value: int) -> None:
        """
        Adds or updates the key,value in LRU cache
        """
        # print(f"put request for key:{key}")
        if key in self.lru_store:
            # 1. search key
            # 2. replace next and prev
            # 3. push the key at tail
            # 4. update k,v in lru_store
            self._search_dll(key)
            # self._print_dll_keys()
            self.lru_store[key] = value
        else: 
            if len(self.lru_store) == self.lru_store_limit:
                # 1. replace head
                # 2. remove old head
                # 3. push the key at tail
                # 4. remove old k,v from store
                # 5. add new k,v in lru_store
                head = self.lru_dll_head
                self.lru_dll_head = self.lru_dll_head.next
                if self.lru_dll_head:
                    self.lru_dll_head.prev = None
                self._add_tail(key)
                del self.lru_store[head.key]
            else:
                # 1. push the key at tail
                # 2. add k,v in lru_store
                self._add_tail(key)
            
            self.lru_store[key] = value
            # print(f"self.lru_store: {self.lru_store}")
            # self._print_dll_keys()




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)