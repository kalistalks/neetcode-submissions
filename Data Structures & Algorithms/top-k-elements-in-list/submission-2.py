class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        sortedfrequency = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        frequencysorted = dict(sortedfrequency)
        result = []
        for number in frequencysorted:
            if len(result) == k:
                break
            result.append(number)

        return result