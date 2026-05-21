class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert_to_recent(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert_to_recent(node)

        if len(self.cache) > self.capacity:
            least_recent = self.left.next
            self.remove(least_recent)
            del self.cache[least_recent.key]

    def remove(self, node: Node) -> None:
        previous = node.prev
        following = node.next
        previous.next = following
        following.prev = previous

    def insert_to_recent(self, node: Node) -> None:
        previous = self.right.prev
        previous.next = node
        node.prev = previous
        node.next = self.right
        self.right.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
