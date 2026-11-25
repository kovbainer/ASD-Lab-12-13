import sys


class Node:

    def __init__(self, item, next_node):
        self.item = item
        self.next = next_node


class Stack:

    def __init__(self):
        self.top = None
        self.count = 0

    def empty(self):
        return self.top is None

    def push(self, item):
        self.top = Node(item, self.top)
        self.count += 1

    def pop(self):
        item = self.top.item
        self.top = self.top.next
        self.count -= 1
        return item

    def back(self):
        return self.top.item

    def size(self):
        return self.count

    def clear(self):
        self.top = None
        self.count = 0


def main():
    stack = Stack()
    out = []
    for line in sys.stdin:
        cmd = line.split()
        if not cmd:
            continue
        if cmd[0] == "push":
            stack.push(cmd[1])
            out.append("ok")
        elif cmd[0] == "pop":
            out.append("error" if stack.empty() else stack.pop())
        elif cmd[0] == "back":
            out.append("error" if stack.empty() else stack.back())
        elif cmd[0] == "size":
            out.append(str(stack.size()))
        elif cmd[0] == "clear":
            stack.clear()
            out.append("ok")
        elif cmd[0] == "exit":
            out.append("bye")
            break
    sys.stdout.write("\n".join(out) + "\n")


main()
