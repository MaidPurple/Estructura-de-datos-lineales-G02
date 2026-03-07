class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, initial_elements=[]):
        self.head = None
        self._length = 0
        for element in initial_elements:
            self.append(element)

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "[" + " -> ".join(elements) + "]"

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if index < 0 or index >= self._length:
            raise IndexError(f"Index {index} is out of range for LinkedList of length {self._length}")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def isEmpty(self):
        return self._length == 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __contains__(self, element):
        for item in self:
            if item == element:
                return True
        return False

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._length += 1

    def insert(self, index, element):
        if index < 0 or index > self._length:
            raise IndexError(f"Index {index} is out of range for LinkedList of length {self._length}")
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._length += 1

    def remove(self, element):
        if self.head is None:
            raise ValueError(f"Element '{element}' not found in LinkedList")
        if self.head.data == element:
            self.head = self.head.next
            self._length -= 1
            return
        current = self.head
        while current.next:
            if current.next.data == element:
                current.next = current.next.next
                self._length -= 1
                return
            current = current.next
        raise ValueError(f"Element '{element}' not found in LinkedList")

    def pop(self, index=-1):
        if self.isEmpty():
            raise IndexError("Pop from empty LinkedList")
        if index < 0:
            index = self._length + index
        if index < 0 or index >= self._length:
            raise IndexError(f"Index {index} is out of range for LinkedList of length {self._length}")
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            self._length -= 1
            return data
        current = self.head
        for _ in range(index - 1):
            current = current.next
        data = current.next.data
        current.next = current.next.next
        self._length -= 1
        return data

    def clear(self):
        self.head = None
        self._length = 0


# ── Quick demo ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    ll = LinkedList([1, 2, 3, 4, 5])

    print("Initial list:   ", ll)
    print("Length:         ", len(ll))
    print("Is empty?       ", ll.isEmpty())
    print("Index 2:        ", ll[2])
    print("Contains 3?     ", 3 in ll)
    print("Contains 99?    ", 99 in ll)

    ll.append(6)
    print("\nAfter append(6):", ll)

    ll.insert(0, 0)
    print("After insert(0, 0):", ll)

    ll.insert(3, 99)
    print("After insert(3, 99):", ll)

    ll.remove(99)
    print("After remove(99):", ll)

    popped = ll.pop(0)
    print(f"After pop(0) → popped={popped}:", ll)

    popped = ll.pop()
    print(f"After pop()  → popped={popped}:", ll)

    print("\nIterating:")
    for item in ll:
        print(" ", item)

    ll.clear()
    print("\nAfter clear():", ll, "| Is empty?", ll.isEmpty())