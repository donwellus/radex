class Node:
    def __init__(self, value=''):
        self.value = value
        self.children = {}


f = open('./geohash-list.txt', 'r')
hashes = f.read().split(' ')

print(hashes)
