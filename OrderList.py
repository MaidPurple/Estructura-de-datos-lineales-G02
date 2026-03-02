class OrderList:

    def __init__(self, initial_elements=[]):
        self._elements = list(initial_elements)
    
    def __str__(self):
        return f"OrderList({self._elements})"
    
    def __len__(self):
        return len(self._elements)
    
    def __getitem__(self, index):
        if index < 0 or index >= len(self._elements):
            raise IndexError(f"Index {index} does not exist in the collection.")
        return self._elements[index]
    
    def isEmpty(self):
        return len(self._elements) == 0
    
    def __iter__(self):
        return iter(self._elements)
    
    def __contains__(self, element):
        return element in self._elements
    
    def add(self, element):
        self._elements.append(element)
    
    def remove(self, element):
        if element not in self._elements:
            raise ValueError(f"Element '{element}' does not exist in the collection.")
        self._elements.remove(element)
    
    def pop(self, index):
        if index < 0 or index >= len(self._elements):
            raise IndexError(f"Index {index} does not exist in the collection.")
        return self._elements.pop(index)

    def clear(self):
        self._elements = []


#prueba
if __name__ == "__main__":
    ol = OrderList([10, 20, 30])
    print("Initial:", ol)
    print("Length:", len(ol))

    #add
    ol.add(40)
    print("After add(40):", ol)

    # __getitem__
    print("Element at index 2:", ol[2])

    # __contains__
    print("20 in list?", 20 in ol)
    print("99 in list?", 99 in ol)

    # isEmpty
    print("Is empty?", ol.isEmpty())

    # __iter__
    print("Iterating:", end=" ")
    for item in ol:
        print(item, end=" ")
    print()

    # remove
    ol.remove(20)
    print("After remove(20):", ol)

    # pop
    popped = ol.pop(0)
    print(f"Popped index 0 ({popped}):", ol)

    # clear
    ol.clear()
    print("After clear:", ol)
    print("Is empty?", ol.isEmpty())

    # Error examples
    print("\n── Error examples ──")
    try:
        ol[5]
    except IndexError as e:
        print("IndexError:", e)

    try:
        ol.remove(99)
    except ValueError as e:
        print("ValueError:", e)