PRIORITY = {"+": 1, "-": 1, "*": 2, "/": 2}
ATOM = 3


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def to_infix(expr):
    stack = Stack()
    for ch in reversed(expr):
        if ch.isalpha():
            stack.push((ch, ATOM))
            continue
        left, lp = stack.pop()
        right, rp = stack.pop()
        p = PRIORITY[ch]
        if lp < p:
            left = "(" + left + ")"
        if rp < p or (rp == p and ch in "-/"):
            right = "(" + right + ")"
        stack.push((left + ch + right, p))
    return stack.pop()[0]


print(to_infix(input().strip()))
