
class TrieNode:
    def __init__(self, value='', terminal=False):
        # Initialize this node in the Trie
        self.is_terminal = terminal
        self.value = value
        self.children = [None for _ in range(26)]

    def insert(self, char):
        # Add a child node in this Trie
        self.children[TrieNode.map_chr(char)] = TrieNode(value=char)

    def suffixes(self, suffix=''):
        suffixes = self._suffixes(suffix)
        if len(suffixes) > 0:
            if suffixes[0] == self.value:
                del suffixes[0]
            for i in range(len(suffixes)):
                if suffixes[i][0] == self.value:
                    suffixes[i] = suffixes[i][1:]
        return suffixes

    def _suffixes(self, suffix):
        suffix = f'{suffix}{self.value}'
        suffixes = list()
        if self.is_terminal:
            suffixes.append(suffix)

        for child in self.children:
            if child is not None:
                suffixes.extend(child._suffixes(suffix))

        return suffixes

    @staticmethod
    def map_chr(char):
        chr_map = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'p': 15,
            'q': 16,
            'r': 17,
            's': 18,
            't': 19,
            'u': 20,
            'v': 21,
            'w': 22,
            'x': 23,
            'y': 24,
            'z': 25}
        return chr_map[char]


# The Trie itself containing the root node and insert/find functions

class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        node = self.root
        for i, v in enumerate(word):
            map_index = TrieNode.map_chr(v)
            if node.children[map_index] is None:
                node.insert(word[i])
            node = node.children[map_index]
            if i == len(word) - 1:
                node.is_terminal = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        node = self.root
        for i, v in enumerate(prefix):
            map_index = TrieNode.map_chr(v)
            if node.children[map_index] is None:
                return None
            node = node.children[map_index]
        return node

    def contains(self, prefix):
        node = self.root
        for i, v in enumerate(prefix):
            map_index = TrieNode.map_chr(v)
            if node.children[map_index] is None:
                return False
            node = node.children[map_index]
        if node.is_terminal:
            return True
        return False


wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

trie = Trie()
for word in wordList:
    trie.insert(word)

cases = ['function', 'funk', 'protagonist', 'tripod', 'fun', 'func']
print('In Trie:', wordList)
for case in cases:
    node = trie.find(case)
    print(case, node)
    if node:
        print(case, node.suffixes())
# https://en.wikipedia.org/wiki/Trie
