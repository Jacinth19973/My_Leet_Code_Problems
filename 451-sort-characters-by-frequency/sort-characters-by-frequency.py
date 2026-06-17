from collections import Counter 
class Solution:
    def frequencySort(self, s: str) -> str:
        string=Counter(s)
        result=[char*freq for char,freq in string.most_common()]
        return "".join(result)  