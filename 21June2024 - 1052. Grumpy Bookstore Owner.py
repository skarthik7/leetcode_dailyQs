class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base_satisfaction = sum(c for c, g in zip(customers, grumpy) if g == 0)
        
        added_satisfaction = 0
        window_satisfaction = 0
        for i in range(len(customers)):
            if grumpy[i] == 1:
                window_satisfaction += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                window_satisfaction -= customers[i - minutes]
            added_satisfaction = max(added_satisfaction, window_satisfaction)
        
        return base_satisfaction + added_satisfaction