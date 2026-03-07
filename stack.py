class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    Stack (LIFO) implementation using a singly linked list.
    The 'top' of the stack is the head of the linked list,
    so push and pop are both O(1).
    """

    def __init__(self, initial_elements=[]):
        self.top = None
        self._length = 0
        # Push each element so the last one ends up on top
        for element in initial_elements:
            self.push(element)

    def __str__(self):
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        # Show top on the left so the visual matches LIFO order
        return "TOP -> [" + " | ".join(elements) + "]"

    def __len__(self):
        return self._length

    def isEmpty(self):
        return self._length == 0

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty Stack")
        return self.top.data

    def __iter__(self):
        current = self.top
        while current:
            yield current.data
            current = current.next

    def __contains__(self, element):
        for item in self:
            if item == element:
                return True
        return False

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self._length += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty Stack")
        data = self.top.data
        self.top = self.top.next
        self._length -= 1
        return data


# ── Quick demo ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    s = Stack([1, 2, 3])

    print("Initial stack:  ", s)
    print("Length:         ", len(s))
    print("Is empty?       ", s.isEmpty())
    print("Peek (top):     ", s.peek())
    print("Contains 2?     ", 2 in s)
    print("Contains 99?    ", 99 in s)

    s.push(4)
    s.push(5)
    print("\nAfter push(4) and push(5):", s)

    popped = s.pop()
    print(f"After pop() → popped={popped}:", s)

    popped = s.pop()
    print(f"After pop() → popped={popped}:", s)

    print("\nIterating (top to bottom):")
    for item in s:
        print(" ", item)