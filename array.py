class ArrayList:
    def __init__(self, size=100, initial_elements=[]):
        if size <= 0:
            raise ValueError("Size must be greater than 0")

        self.capacity = size
        self.data = [None] * self.capacity
        self.count = 0

        for element in initial_elements:
            self.append(element)

    def __str__(self):
        result = "["
        for i in range(self.count):
            result += str(self.data[i])
            if i < self.count - 1:
                result += ", "
        result += "]"
        return result

    def __len__(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def __getitem__(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index does not exist")
        return self.data[index]

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index < self.count:
            value = self.data[self._iter_index]
            self._iter_index += 1
            return value
        else:
            raise StopIteration

    def __contains__(self, element):
        for i in range(self.count):
            if self.data[i] == element:
                return True
        return False

    def append(self, element):
        if self.count >= self.capacity:
            raise OverflowError("ArrayList is full")

        self.data[self.count] = element
        self.count += 1

    def insert(self, index, element):
        if index < 0 or index > self.count:
            raise IndexError("Index does not exist")

        if self.count >= self.capacity:
            raise OverflowError("ArrayList is full")

        i = self.count
        while i > index:
            self.data[i] = self.data[i - 1]
            i -= 1

        self.data[index] = element
        self.count += 1

    def remove(self, element):
        index = -1
        for i in range(self.count):
            if self.data[i] == element:
                index = i
                break

        if index == -1:
            raise ValueError("Element does not exist in the collection")

        self.pop(index)

    def pop(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index does not exist")

        removed = self.data[index]

        i = index
        while i < self.count - 1:
            self.data[i] = self.data[i + 1]
            i += 1

        self.data[self.count - 1] = None
        self.count -= 1

        return removed

    def clear(self):
        i = 0
        while i < self.count:
            self.data[i] = None
            i += 1
        self.count = 0


# Crear la lista (usa __init__)
lista = ArrayList(10, [1, 2, 3])

# Mostrar la lista (usa __str__)
print("Lista inicial:", lista)

# Obtener tamaño (usa __len__)
print("Tamaño:", len(lista))

# Verificar si está vacía (usa isEmpty)
print("¿Está vacía?", lista.isEmpty())

# Acceder a un elemento por índice (usa __getitem__)
print("Elemento en índice 1:", lista[1])

# Agregar un elemento al final (usa append)
lista.append(4)
print("Después de append:", lista)

# Insertar un elemento en una posición específica (usa insert)
lista.insert(2, 99)
print("Después de insert:", lista)

# Verificar si un elemento existe (usa __contains__)
print("¿El 99 está en la lista?", 99 in lista)

# Recorrer la lista con for (usa __iter__ y __next__)
print("Recorriendo la lista:")
for elemento in lista:
    print(elemento)

# Eliminar un elemento por su valor (usa remove)
lista.remove(99)
print("Después de remove(99):", lista)

# Eliminar un elemento por índice y retornarlo (usa pop)
eliminado = lista.pop(1)
print("Elemento eliminado con pop:", eliminado)
print("Después de pop:", lista)

# Vaciar completamente la lista (usa clear)
lista.clear()
print("Después de clear:", lista)

# Verificar nuevamente si está vacía (usa isEmpty)
print("¿Está vacía ahora?", lista.isEmpty())