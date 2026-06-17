class Solution:
    def subStrHash(self, s: str, p: int, m: int, k: int, hashValue: int) -> str:
        n = len(s)
        vals = [ord(c) - 96 for c in s]
        pk = pow(p, k, m)
        cur = 0
        res = n
        for i in range(n - 1, -1, -1):
            cur = (cur * p + vals[i]) % m
            if i + k < n:
                cur = (cur - vals[i + k] * pk) % m
            if cur == hashValue:
                res = i      
        return s[res : res + k]
