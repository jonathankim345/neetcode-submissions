class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        left = 0 
        res = []
        while left < len(s):
            right = left 
            while s[right] != '#':
                right += 1 
            number = int(s[left:right])
            left = right + 1
            res.append(s[left:left + number])
            left += number
        return res
