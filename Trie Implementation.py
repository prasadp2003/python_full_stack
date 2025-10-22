# Node class representing each character in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}   # Dictionary to store child nodes
        self.is_end = False  # Marks the end of a word


# Trie class for inserting, searching, and prefix checking
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    # Search for a complete word
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    # Check if any word starts with a given prefix
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
