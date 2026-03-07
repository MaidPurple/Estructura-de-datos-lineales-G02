class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self, initial_elements=[]):
        self.head = None   # front of the queue  (next to be popped)
        self.tail = None   # back of the queue   (last pushed)
        self._length = 0
        for element in initial_elements:
            self.push(element)

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "FRONT -> [" + " | ".join(elements) + "] <- BACK"

    def __len__(self):
        return self._length

    def isEmpty(self):
        return self._length == 0

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty Queue")
        return self.head.data

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

    def push(self, element):
        """Enqueue: add element to the back of the queue."""
        new_node = Node(element)
        if self.tail is None:          # queue was empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def pop(self):
        """Dequeue: remove and return the front element (FIFO)."""
        if self.isEmpty():
            raise IndexError("Pop from empty Queue")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:          # queue is now empty
            self.tail = None
        self._length -= 1
        return data


# ── Quick demo ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    q = Queue([1, 2, 3])

    print("Initial queue:  ", q)
    print("Length:         ", len(q))
    print("Is empty?       ", q.isEmpty())
    print("Peek (front):   ", q.peek())
    print("Contains 2?     ", 2 in q)
    print("Contains 99?    ", 99 in q)

    q.push(4)
    q.push(5)
    print("\nAfter push(4) and push(5):", q)

    popped = q.pop()
    print(f"After pop() → popped={popped}:", q)

    popped = q.pop()
    print(f"After pop() → popped={popped}:", q)

    print("\nIterating (front to back):")
    for item in q:
        print(" ", item)