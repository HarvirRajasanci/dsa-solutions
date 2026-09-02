class RandomizedSet:

    def __init__(self):
        self.elements = []
        self.indexes = {}

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        self.elements.append(val)
        self.indexes[val] = len(self.elements) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        idx = self.indexes[val]
        last = self.elements[-1]

        self.elements[idx] = last
        self.indexes[last] = idx

        self.elements.pop()
        self.indexes.pop(val)
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.elements)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()