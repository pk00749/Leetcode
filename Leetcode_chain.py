

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

    def get_value(self, position):
        current = self.head
        p = 1

        if position > self.get_length():
            print("Exceed the length")
            return 0

        while p != position:
            current = current.get_next()
            p += 1
        else:
            return current.get_value()

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
# print(chain.isEmpty())
chain.add('A')
chain.add('B')
chain.add('C')
# chain.insert('3', 3)
# chain.insert('4', 3)
# chain.modify('4', '10')
# chain.remove('4')
# print(chain.get_length())
# print(chain.get_value(5))
# chain.print()

chain_1 = Chain()
chain_1.add(1)
chain_1.add(2)
chain_2 = Chain()
# chain_2.add(3)
chain_2.add(4)

def add_two_chain(chain_1, chain_2):

    if chain_1 is None or chain_2 is None:
        return 0

    head_1 = chain_1.head
    head_2 = chain_2.head
    carry = 0

    while head_1.get_next() is not None or head_2.get_next() is not None:
        print(head_1.get_value())
        print(head_1.get_next())
        print(head_2.get_value())
        print(head_2.get_next())

        if head_1.get_next() is None:
            head_1.set_next(Node(0))
            print("add 1")

        if head_2.get_next() is None:
            head_2.set_next(Node(0))
            print("add 2")
        print("----------------")

        tmp = head_1.get_value() + head_2.get_value() + carry
        carry = tmp // 10
        head_1.set_value(tmp%10)
        # print(carry, tmp, head_1.get_value())

        head_1 = head_1.get_next()
        head_2 = head_2.get_next()
    else:
        return 0
    # else:
    #     head_1 = head_1.get_value() + head_2.get_value() + carry
    #     if head_1 > 10:
    #         head_1 = head_1 % 10
    #         head_1.set_next(Node(1))

add_two_chain(chain_1, chain_2)
# h = chain_2.head
# print(h.get_next())
# if h.get_next() is None:
#     h.set_next(Node(0))
#
# print(h.get_next())
# h=h.get_next()
# print(h.get_value())

# def test(text):
#     node = text.head
#     print(node.get_next())
#
# test(chain_2)

