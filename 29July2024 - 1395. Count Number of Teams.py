# Two solutions listed below, one with O(n^3) and the other with O(n^2) time complexity.

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        # Iterate through all combinations of three soldiers
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        count += 1
        
        return count

# Time complexity: O(n^3)

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        for j in range(n):
            left_smaller = left_larger = right_smaller = right_larger = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_larger += 1
            
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                elif rating[k] > rating[j]:
                    right_larger += 1
            
            count += left_smaller * right_larger + left_larger * right_smaller
        
        return count
    
# Time Complexity: (O(n^2)) because we use two nested loops to count the smaller and larger elements for each soldier.