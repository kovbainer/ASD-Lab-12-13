class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def is_correct(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for ch in s:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.empty() or stack.pop() != pairs[ch]:
                return False
    return stack.empty()


try:
    s = input().strip()
except EOFError:
    s = ""
print("yes" if is_correct(s) else "no")
