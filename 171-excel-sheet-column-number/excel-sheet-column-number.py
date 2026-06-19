class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0        
        for char in columnTitle:
            value = ord(char) - 64            
            result = result * 26 + value
        return result
