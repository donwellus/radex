class Node:
    def __init__(self, value=''):
        self.value = value
        self.children = {}


class Tree:
    def __init__(self):
        self.root = Node()


f = open('./geohash-list.txt', 'r')
hashes = f.read().split(' ')

print(hashes)
