# https://leetcode.com/problems/most-beautiful-item-for-each-query/
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        
        prices = []
        max_beauty = []
        curr_max = 0
        
        for price, beauty in items:
            curr_max = max(curr_max, beauty)
            if not prices or price != prices[-1]:
                prices.append(price)
                max_beauty.append(curr_max)
            else:
                max_beauty[-1] = curr_max
        
        def binary_search(target):
            left, right = 0, len(prices) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                if prices[mid] <= target:
                    result = mid    
                    left = mid + 1
                else:
                    right = mid - 1
            
            return max_beauty[result] if result != -1 else 0
        return [binary_search(q) for q in queries]
# time complexity: O(n log n) for sorting + O(m log n) for binary search = O((n+m) log n)
