# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_cp = last_cp = prev_cp = -1
        min_dist = float('inf')
        i = 0
        current = head.next
        prev = head
        
        while current and current.next:
            if (current.val > prev.val and current.val > current.next.val) or \
               (current.val < prev.val and current.val < current.next.val):
                if first_cp == -1:
                    first_cp = i
                else:
                    min_dist = min(min_dist, i - prev_cp)
                last_cp = i
                prev_cp = i
            
            prev = current
            current = current.next
            i += 1
        if first_cp == -1 or last_cp == -1 or first_cp == last_cp:
            return [-1, -1]
        
        max_dist = last_cp - first_cp
        min_dist = min_dist if min_dist != float('inf') else -1
        return [min_dist, max_dist]
    
# Time complexity: O(N)