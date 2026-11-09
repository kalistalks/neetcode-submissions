class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero = 1, 0 
        for i in nums: 
            if i:
                product *= i 
            else: 
                zero += 1 
        if zero > 1: return [0] * len(nums)

        result = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero:
                if c:
                    result[i] = 0
                else: 
                    result[i] = product
            else: 
                result[i] = product // c
        return result
        