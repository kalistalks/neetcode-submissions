class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for number in nums[k:]: 
            if number > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, number)

        return min_heap[0]