class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        r = len(digits)-1
            
        digits[r] += 1
        while digits[r] >= 10:
            digits[r] %= 10
            r -= 1
            if r >= 0:
                digits[r] += 1
            else:
                digits.insert(0, 1)
        return digits
                
                