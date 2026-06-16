class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            return functools.reduce(lambda ans, c: ans[:-1] if c == '#' else ans + c, string, '')
        return build(s) == build(t)
