from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        results = []

        for i in range(len(sort_nums) - 2):
            num = sort_nums[i]

            # Skip duplicate first numbers.
            if i > 0 and num == sort_nums[i - 1]:
                continue

            # All remaining numbers are positive.
            if num > 0:
                break

            l, r = i + 1, len(sort_nums) - 1
            target = -num

            while l < r:
                temp_sum = sort_nums[l] + sort_nums[r]

                if temp_sum > target:
                    r -= 1
                elif temp_sum < target:
                    l += 1
                else:
                    results.append([num, sort_nums[l], sort_nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicate second and third numbers.
                    while l < r and sort_nums[l] == sort_nums[l - 1]:
                        l += 1
                    while l < r and sort_nums[r] == sort_nums[r + 1]:
                        r -= 1

        return results