# Dynamic Array implementation
# Note: Python lists are dynamic arrays by default,
# but this is an example of what's going on under the hood.
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    # Get value at i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    # Insert n at i-th index
    def insert(self, i: int, n: int) -> None:
        self.arr[i] = n

    # Insert n in the last position of the array
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
            
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    # Remove the last element in the array
    def popback(self) -> int:
        if self.length > 0:
            # soft delete the last element
            self.length -= 1
        # return the popped element
        return self.arr[self.length]

    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity 
        
        # Copy elements to new_arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity

my_array = DynamicArray(5)
my_array.pushback(10)
my_array.pushback(20)
my_array.pushback(30)

my_array.insert(1, 15)

print("Size:", my_array.getSize())
print("Capacity:", my_array.getCapacity())

print("Value at index 2:", my_array.get(2))

popped_value = my_array.popback()
print("Popped value:", popped_value)