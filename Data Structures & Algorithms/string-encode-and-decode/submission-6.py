class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res = res + str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            num = ""
            while i < len(s) and s[i].isdigit():
                num = num + s[i]
                i += 1
            i += 1
            num = int(num)
            res.append(s[i:i + num])
            i += num
        return res