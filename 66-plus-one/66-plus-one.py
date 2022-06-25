class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1

        else:
            index = -1

            for i in reversed(digits):
                value = i + carry

                if value <= 10:
                    digits[index] = value % 10
                    carry = value // 10

                else:
                    digits[index] = i + carry
                index -= 1


            [digits.insert(0, carry) if carry > 0 else digits]

        return digits
        