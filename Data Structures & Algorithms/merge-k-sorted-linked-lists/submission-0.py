# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i in range(len(lists)):
            head = lists[i]
            if head is not None: 
                heapq.heappush(min_heap, (head.val, i, head))
                # pushes in (priority, data) where data is the lists[i] and ListNode

        result = ListNode()
        current = result 

        while min_heap: 
            _, list_index, node = heapq.heappop(min_heap)

            current.next = node
            current = current.next 

            if node.next is not None: 
                heapq.heappush(min_heap, (node.next.val, list_index, node.next))

        current.next = None 

        return result.next 
