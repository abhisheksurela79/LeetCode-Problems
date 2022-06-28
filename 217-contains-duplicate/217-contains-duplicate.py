class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newNums = set(nums)

        return [False if len(newNums) == len(nums) else True][0]
