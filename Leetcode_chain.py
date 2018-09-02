

class Node:
    def __init__(self, value):
        self.value = value
        self.next = 0

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def set_next(self, next):
        self.next = next

    def set_value(self, value):
        self.value = value

class Chain:
    def __init__(self):
        self.head = None

    def add(self,item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def insert(self, item, position):
        node = Node(item)
        current = self.head
        previous = None
        p = 1

        while p < position:
            previous = current
            current = current.get_next()
            p += 1
        else:
            node.set_next(current)
            previous.set_next(node)

    def print(self):
        node = self.head
        print("Head >", node.get_value())
        node = node.get_next()
        while node:
            print(">", node.get_value())
            node = node.get_next()
        else:
            print("End >", node)


chain = Chain()
chain.add('A')
chain.add('B')
chain.add('C')
chain.insert('3', 3)
chain.insert('4', 3)
chain.print()
