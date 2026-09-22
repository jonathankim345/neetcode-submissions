class PrefixNode:
    def __init__(self, val):
        self.val = val
        self.next = {}
        self.last = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode("")

    def insert(self, word: str) -> None:
        # if root is None:
        #     print("Root is None")
        curr = self.root
        for char in word: 
            if char not in curr.next: 
                curr.next[char] = PrefixNode(char)
            curr = curr.next[char]
        curr.last = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word: 
            if char not in curr.next: 
                return False
            curr = curr.next[char]
        if curr.last == True:
            return True
        else: 
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix: 
            if char not in curr.next: 
                return False
            curr = curr.next[char]
        return True