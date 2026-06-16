from collections import Counter
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        c_counts = Counter(chars)
        return sum(len(w) for w in words if not Counter(w) - c_counts)
