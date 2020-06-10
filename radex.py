from functools import reduce


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

    def regex(self, node=None):
        if node is None:
            node = self.root

        if len(node.children) < 1:
            return node.value

        children = []
        for c in node.children:
            children.append(self.regex(node.children[c]))

        if reduce((lambda x, y: x or y), ['[' in s for s in children]):
            re = '|'.join(children)
            re = '(' + re + ')'
        else:
            re = ''.join(children)
            re = '[' + re + ']'
        return node.value + re


f = open('./geohash-list.txt', 'r')
hashes = f.read().split(' ')

print(hashes)

tree = Tree()
for hash in hashes:
    tree.insert(hash)
