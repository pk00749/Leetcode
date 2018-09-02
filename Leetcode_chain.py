

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

    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def insert(self, item, position):
        if self.get_length() > 0:
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

    def remove(self, item):
        current = self.head
        previous = Node(None)

        while current.get_value() != item:
            previous = current
            if current.get_next() is not None:
                current = current.get_next()
            else:
                print("No this value so that cannot remove")
                break
        else:
            previous.set_next(current.get_next())

    def modify(self, before, after):
        current = self.head
        while current.get_value() != before:
            current = current.get_next()
        else:
            current.set_value(after)

    def get_length(self):
        current = self.head
        chain_len = 0
        while current:
            current = current.get_next()
            chain_len += 1
        return chain_len

    def isEmpty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

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
print(chain.isEmpty())
chain.add('A')
chain.add('B')
chain.add('C')
chain.insert('3', 3)
chain.insert('4', 3)
chain.modify('4', '10')
chain.remove('4')
print(chain.get_length())
chain.print()
