class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return "".join([s[indices.index(_)] for _ in range(len(s))])