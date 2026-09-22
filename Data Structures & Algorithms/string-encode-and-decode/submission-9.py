class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded = encoded + str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        l = 0
        res = [] 
        while l < len(s):
            r = l + 1
            while s[r] != '#':
                r += 1
            number = int(s[l:r])
            print(number)
            word = s[r + 1:r + 1 + number]
            print(word)
            res.append(word)
            l = r + 1 + number
            print(l)
        return res
        