class TrieNode:

    def __init__(self):
        self.chidren = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.chidren:
                node.chidren[char] = TrieNode()
            node = node.chidren[char]

        node.end = True

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(i: int, node: TrieNode):
            if i == len(word) and node.end:
                return True
            if i == len(word):
                return False
            if word[i] not in node.chidren and word[i] != ".":
                return False

            if word[i] == ".":
                for child in node.chidren.values():
                    if dfs(i + 1, child):
                        return True
                return False
                        
            else:
                node = node.chidren[word[i]]
                return dfs(i + 1, node)

        return dfs(0, node)
