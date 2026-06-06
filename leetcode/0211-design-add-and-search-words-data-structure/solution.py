class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.is_word

            char = word[index]

            if char == ".":
                return any(dfs(index + 1, child) for child in node.children.values())

            if char not in node.children:
                return False

            return dfs(index + 1, node.children[char])

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
