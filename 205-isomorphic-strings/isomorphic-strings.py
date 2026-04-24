class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zip(s,t)
        set(zip(s,t))
        return len(set(s))==len(set(t))==len(set(zip(s,t)))
