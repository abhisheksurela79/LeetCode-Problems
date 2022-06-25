class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        flag = 0

        if target in nums:
            flag = nums.index(target)

        elif nums[0] > target:
            flag = 0

        elif nums[-1] < target:
            flag = len(nums)

        else:
            for _ in enumerate(nums):

                if _[1] < target:
                    flag = _[0]

                elif _[1] > target:
                    flag = _[0]

                    break

        return flag
        