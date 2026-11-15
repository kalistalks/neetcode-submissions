class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        map = defaultdict(list)
        result = set() 

        for j in range(len(nums)):
            for k in range(j + 1, len(nums)):

                value = -1 * (nums[j] + nums[k])

                if value in map: 
                    result.add(tuple(sorted([value, nums[j], nums[k]])))

            map[nums[j]].append(j)

        return list(result)