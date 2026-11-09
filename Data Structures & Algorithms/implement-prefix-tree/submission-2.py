class TrieNode:

    def __init__(self):
        self.chidren = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.chidren:
                node.chidren[char] = TrieNode()
            node = node.chidren[char]

        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.chidren:
                return False
            node = node.chidren[char]
        return node.end
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.chidren:
                return False
            node = node.chidren[char]
        return True

        