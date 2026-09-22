import random
class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index: 
            return False
        else: 
            self.val_to_index[val] = len(self.array)
            self.array.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.val_to_index: 
            index = self.val_to_index[val]
            last = self.array[-1]
            self.array[-1] = val
            self.array[index] = last
            self.val_to_index[last] = index
            self.array.pop()
            del self.val_to_index[val]
            return True 
        else: 
            return False 

    def getRandom(self) -> int:
        random_choice = random.choice(self.array)
        return random_choice
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()