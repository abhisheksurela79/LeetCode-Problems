class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        newNums = list(set(nums))

        number = 0
        counts = 0

        for i in enumerate(newNums):
            currentCount = nums.count(i[1])

            if currentCount > counts:
                counts = currentCount
                number = newNums[i[0]]

            else:
                continue



        return number
        