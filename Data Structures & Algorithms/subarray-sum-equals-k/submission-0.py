class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {}
        result = 0 
        currentSum = 0 

        for number in nums: 
            currentSum += number

            if currentSum == k: 
                result += 1 

            if currentSum - k in prefixSums: 
                result += prefixSums[currentSum - k]

            prefixSums[currentSum] = prefixSums.get(currentSum, 0) + 1 

        return result 