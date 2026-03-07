class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    """
    Circular Linked List implementation.
    - A single 'tail' pointer is kept; tail.next is always the HEAD.
    - All operations maintain the circular invariant.
    """

    def __init__(self, initial_elements=[]):
        self.tail = None       # tail.next == head
        self._length = 0
        for element in initial_elements:
            self.append(element)

    # ── helpers ──────────────────────────────────────────────────────────────

    @property
    def _head(self):
        return self.tail.next if self.tail else None

    def _node_at(self, index):
        """Return the node at a given index (no bounds check here)."""
        current = self._head
        for _ in range(index):
            current = current.next
        return current

    # ── dunder methods ───────────────────────────────────────────────────────

    def __str__(self):
        if self.isEmpty():
            return "[]"
        elements = []
        current = self._head
        for _ in range(self._length):
            elements.append(str(current.data))
            current = current.next
        return "[" + " -> ".join(elements) + " -> (back to start)]"

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if index < 0 or index >= self._length:
            raise IndexError(
                f"Index {index} is out of range for CircularList of length {self._length}"
            )
        return self._node_at(index).data

    def isEmpty(self):
        return self._length == 0

    def __iter__(self):
        if self.isEmpty():
            return
        current = self._head
        for _ in range(self._length):
            yield current.data
            current = current.next

    def __contains__(self, element):
        for item in self:
            if item == element:
                return True
        return False

    # ── mutation methods ─────────────────────────────────────────────────────

    def append(self, element):
        """Add element to the end (new tail)."""
        new_node = Node(element)
        if self.isEmpty():
            new_node.next = new_node        # points to itself
            self.tail = new_node
        else:
            new_node.next = self._head      # new node points to old head
            self.tail.next = new_node       # old tail points to new node
            self.tail = new_node            # advance tail
        self._length += 1

    def add(self, index, element):
        """Insert element at the requested index."""
        if index < 0 or index > self._length:
            raise IndexError(
                f"Index {index} is out of range for CircularList of length {self._length}"
            )
        if index == self._length:           # same as append
            self.append(element)
            return
        new_node = Node(element)
        if index == 0:                      # insert before current head
            new_node.next = self._head
            self.tail.next = new_node
        else:
            prev = self._node_at(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self._length += 1

    def remove(self, element):
        """Remove the first occurrence of element by value."""
        if self.isEmpty():
            raise ValueError(f"Element '{element}' not found in CircularList")

        current = self._head
        prev = self.tail                    # circular: prev of head is tail

        for _ in range(self._length):
            if current.data == element:
                if self._length == 1:       # only one node
                    self.tail = None
                else:
                    prev.next = current.next
                    if current is self.tail:
                        self.tail = prev    # removed the tail; update it
                self._length -= 1
                return
            prev = current
            current = current.next

        raise ValueError(f"Element '{element}' not found in CircularList")

    def pop(self, index=-1):
        """Remove and return the element at the given index."""
        if self.isEmpty():
            raise IndexError("Pop from empty CircularList")
        if index < 0:
            index = self._length + index
        if index < 0 or index >= self._length:
            raise IndexError(
                f"Index {index} is out of range for CircularList of length {self._length}"
            )

        if self._length == 1:
            data = self.tail.data
            self.tail = None
            self._length -= 1
            return data

        if index == 0:                      # remove head
            data = self._head.data
            self.tail.next = self._head.next
        else:
            prev = self._node_at(index - 1)
            target = prev.next
            data = target.data
            prev.next = target.next
            if target is self.tail:         # removed the tail; update it
                self.tail = prev

        self._length -= 1
        return data

    def clear(self):
        self.tail = None
        self._length = 0


# ── Quick demo ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cl = CircularList([1, 2, 3, 4, 5])

    print("Initial list:      ", cl)
    print("Length:            ", len(cl))
    print("Is empty?          ", cl.isEmpty())
    print("Index 0:           ", cl[0])
    print("Index 4:           ", cl[4])
    print("Contains 3?        ", 3 in cl)
    print("Contains 99?       ", 99 in cl)

    cl.append(6)
    print("\nAfter append(6):   ", cl)

    cl.add(0, 0)
    print("After add(0, 0):   ", cl)

    cl.add(3, 99)
    print("After add(3, 99):  ", cl)

    cl.remove(99)
    print("After remove(99):  ", cl)

    popped = cl.pop(0)
    print(f"After pop(0) → {popped}:", cl)

    popped = cl.pop()
    print(f"After pop()  → {popped}:", cl)

    print("\nIterating:")
    for item in cl:
        print(" ", item)

    cl.clear()
    print("\nAfter clear():     ", cl, "| Is empty?", cl.isEmpty())