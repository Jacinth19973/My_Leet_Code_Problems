class Solution:
    def processStr(self, s: str, k: int) -> str:
        sizes = []
        size = 0
        
        for i in s:
            if i == "*":
                if size > 0:
                    size -= 1
            elif i == "#":
                size *= 2
            elif i == "%":
                pass  
            elif 'a' <= i <= 'z':
                size += 1
            sizes.append(size)
            
        if k < 0 or k >= size:
            return "."
            
        for idx in range(len(s) - 1, -1, -1):
            i = s[idx]
            current_size = sizes[idx]
            
            if i == "%":
                k = current_size - 1 - k
            elif i == "#":
                half = current_size // 2
                if k >= half:
                    k -= half
            elif i == "*":
                continue
            elif 'a' <= i <= 'z':
                if k == current_size - 1:
                    return i
                    
        return "."
