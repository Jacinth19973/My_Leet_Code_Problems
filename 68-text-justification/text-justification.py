from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)
        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            num_words = j - i
            line = ""
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - sum(len(word) for word in words[i:j])
                spaces_between = num_words - 1
                space_each = total_spaces // spaces_between
                extra_spaces = total_spaces % spaces_between

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (space_each + (1 if extra_spaces > 0 else 0))
                    if extra_spaces > 0:
                        extra_spaces -= 1

                line += words[j - 1]

            res.append(line)
            i = j

        return res
