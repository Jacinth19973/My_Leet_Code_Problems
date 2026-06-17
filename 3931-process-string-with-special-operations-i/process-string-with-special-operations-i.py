class Solution:
    def processStr(self, s: str) -> str:
        string=[]
        for i in s:
            if i=="*":
                if string:
                    string.pop()
            elif i=="#":
                string+=string
            elif i=="%":
                string.reverse()
            elif 'a'<= i <='z':
                string+=i
        return "".join(string)