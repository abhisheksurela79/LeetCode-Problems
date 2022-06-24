class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0

        for _ in operations:
            if "-" in _:
                output -= 1
            else:
                output += 1
                
        return output