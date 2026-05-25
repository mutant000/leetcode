class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, text: str):
        node = self
        for char in text:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
