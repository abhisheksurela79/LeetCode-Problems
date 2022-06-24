class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output = 0
        for i in accounts:
            temp = 0
            for j in range(len(i)):
                temp += i[j]

            if temp >= output:
                output = temp

        return output