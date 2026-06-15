class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        s1_breaks_s2 = True
        s2_breaks_s1 = True
        for c1, c2 in zip(s1_sorted, s2_sorted):
            if c1 < c2:
                s1_breaks_s2 = False  
            if c2 < c1:
                s2_breaks_s1 = False  
        return s1_breaks_s2 or s2_breaks_s1