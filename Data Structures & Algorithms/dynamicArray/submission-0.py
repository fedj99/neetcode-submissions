class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._array = []


    def get(self, i: int) -> int:
        return self._array[i]


    def set(self, i: int, n: int) -> None:
        self._array[i] = n


    def pushback(self, n: int) -> None:
        if len(self._array) >= self.capacity:
            self.resize()
        self._array.append(n)


    def popback(self) -> int:
        return self._array.pop()
 

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return len(self._array)
        
    
    def getCapacity(self) -> int:
        return self.capacity
