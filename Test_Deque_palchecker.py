from pythonds.basic.deque import Deque

def palchecker(target):
    depue = Deque()

    for c in target:
        depue.addRear(c)

    while depue.size() > 0:
        if depue.removeFront() == depue.removeRear():
            continue
        else:
            print("It is not pal")
            break
    else:
        print("It is pal")

palchecker('abcddcba')