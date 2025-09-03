class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        def canShip(capacity):
            day_count = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > capacity:
                    day_count += 1
                    current_weight = 0
                current_weight += w
            return day_count <= days
        
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
