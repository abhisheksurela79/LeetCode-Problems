class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        sums = []
        for i in nums:
            temp += i
            sums.append(temp)

        return sums