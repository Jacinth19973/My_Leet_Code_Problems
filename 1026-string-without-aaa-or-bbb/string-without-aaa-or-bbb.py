class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans=[]
        while a>0 and b>0:
            if a>b:
                ans.append("aab")
                a,b=a-2,b-1
            elif b>a:
                ans.append("bba")
                a,b=a-1,b-2
            else:
                ans.append("ab")
                a,b=a-1,b-1
        if a>0: 
            ans.append("a" *a)
        if b>0:
            ans.append("b"*b)
        return "".join(ans)
        