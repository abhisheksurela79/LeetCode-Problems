class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        sum = []


        for i in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += i
            sum.append(current_sum)

        return max(sum)

