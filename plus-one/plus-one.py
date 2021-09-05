class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#         digits[-1] += 1
#         # if digits[-1] >= 10:
#         #     digits.append(digits[-1] % 10)
#         #     digits[-2] = 1
        
#         if digits[-1] >= 10:
            
#         return digits

        # return list(str(int(''.join([str(x) for x in digits])) + 1))
    

#         r = len(digits)-1
#         if digits[r]+1 >= 10:
#             digits.append((digits[r]+1)%10)
#             digits[r] = 1
#             r -= 1

#             while r >= 0:
#                 if digits[r]+1 >= 10:
#                     digits[r] = (digits[r]+1)%10
#                     r -= 1
#                 else:
#                     digits[r] += 1
            
#         else:
#             digits[r] += 1
            
#         return digits

        r = len(digits)-1
#         if digits[r] + 1 < 10:
#             return digits[0:r-1] + [digits[r]+1]
#         else:
            
        digits[r] += 1
        while digits[r] >= 10:
            # if nums[r]+1 < 10:
            #     nums[r]+=1
            #     break
            # else:
            #     nums[r] = (nums[r]+1) % 10
            digits[r] %= 10
            r -= 1
            if r >= 0:
                digits[r] += 1
            else:
                digits.insert(0, 1)
        return digits
                
                