from itertools import chain

def autocomplete_naive(arr, s):
    return list(x for x in arr if x.startswith(s))

def create_autocomplete_trie(arr):
    trie = Trie()
    for w in arr:
        trie.insert(w)
    return trie

class Node:

    def __init__(self, character):
        self.character = character
        self.children = {}
        self.word = False
    
    def add(self, child_node):
        self.children[child_node.character] = child_node

    def autocomplete_subtree(self, prefix):
        if not prefix:
            return self
        n = self.children.get(prefix[0], None)
        return n.autocomplete_subtree(prefix[1:]) if n else None
    
    def gather_words(self, prefix):
        def f(n):
            return n.gather_words(prefix + self.character)
        child_words = list(chain.from_iterable(map(f, self.children.values())))
        if self.word:
            return [prefix + self.character] + child_words
        return child_words

class Trie:
    def __init__(self):
        self._root = Node(None)
    
    def insert(self, word):
        self.__insert(word, self._root).word = True
    
    def __insert(self, word, node):
        if not word:
            return node
        n = node.children.get(word[0], None)
        if not n:
            n = Node(word[0])
            node.add(n)
        return self.__insert(word[1:], n)
    
    def autocomplete(self, prefix):
        subtree = self._root.autocomplete_subtree(prefix)
        return subtree.gather_words(prefix[:-1])
        
    
