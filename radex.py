class Node:
    def __init__(self, value=''):
        self.value = value
        self.children = {}


class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, word, node=None):
        if len(word) < 1:
            return None

        if node is None:
            node = self.root

        c = word[0]
        if c in node.children:
            return self.insert(word[1:], node.children[c])
        else:
            node.children.update({c: Node(c)})
            return self.insert(word[1:], node.children[c])


f = open('./geohash-list.txt', 'r')
hashes = f.read().split(' ')

print(hashes)
