class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        data = [list(jewels), list(stones)]

        count = 0
        for _ in stones:
            if _ in data[0]:
                count += 1

        return count