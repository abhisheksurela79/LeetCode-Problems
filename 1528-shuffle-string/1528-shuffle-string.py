class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x = ""
        
        for _ in range(len(s)):
            x += s[indices.index(_)]
            
        return x