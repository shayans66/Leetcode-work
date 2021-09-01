class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#         digits[-1] += 1
#         # if digits[-1] >= 10:
#         #     digits.append(digits[-1] % 10)
#         #     digits[-2] = 1
        
#         if digits[-1] >= 10:
            
#         return digits

        return list(str(int(''.join([str(x) for x in digits])) + 1))