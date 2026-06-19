class Solution:
    def reverseVowels(self, s: str) -> str:
        inp=list(s)
        vowels=set("aeiouAEIOU")
        left,right=0,len(s)-1
        while left<right:
            while left<right and inp[left] not in vowels:
                left=left+1
            while left<right and inp[right] not in vowels:
                right=right-1
            inp[left],inp[right]=inp[right],inp[left]
            left+=1
            right-=1
        return "".join(inp)
