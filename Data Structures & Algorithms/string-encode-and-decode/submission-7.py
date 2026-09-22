class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded = encoded + str(len(s)) + "#" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        l, r = 0, 0
        while l < len(s):
            while s[r] != "#":
                r += 1
            num = int(s[l:r])
            decoded.append(s[r + 1:r + 1 + num])
            l = r + num + 1
            r = l + 1
        # We have 5#Hello5#World 
        # Then we have 0 1 2 3 4 6 7
        return decoded