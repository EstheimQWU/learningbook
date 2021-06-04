class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = 0
        for i in range(len(digits)):
            if digits[-(i + 1)] == 9:
                length = length + 1
                continue
            else:
                break
        if length == 0:
            digits[-1] = digits[-1] + 1
            return digits
        elif length == len(digits):
            # 在第一位插1
            digits.insert(0, 1)
            for i in range(length):
                digits[i+1] = 0
            return digits
        else:
            digits[-(length + 1)] = digits[-(length + 1)] + 1
            for i in range(length):
                digits[-(i + 1)] = 0
            return digits
