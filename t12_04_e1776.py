import sys


class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]


def possible(order, n):
    station = Stack()
    nxt = 1
    for car in order:
        while nxt <= n and (station.empty() or station.top() != car):
            station.push(nxt)
            nxt += 1
        if station.empty() or station.top() != car:
            return False
        station.pop()
    return True


def main():
    data = sys.stdin.read().split()
    pos = 0
    out = []
    while pos < len(data):
        n = int(data[pos])
        pos += 1
        if n == 0:
            break
        while pos < len(data):
            first = int(data[pos])
            if first == 0:
                pos += 1
                break
            order = [int(x) for x in data[pos:pos + n]]
            pos += n
            out.append("Yes" if possible(order, n) else "No")
        out.append("")
    sys.stdout.write("\n".join(out) + "\n")


main()
