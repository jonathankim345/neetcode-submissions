class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        left = 0 
        right = left + 1
        res = []
        while right < len(s):
            while s[right] != '#':
                right += 1 
            number = int(s[left:right])
            res.append(s[right + 1:right + number + 1])
            left = right + number + 1
            right = left + 1
        return res
