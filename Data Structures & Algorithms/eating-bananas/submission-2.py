class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)

        min_speed = float('inf')
        while L <= R:
            mid = L + (R - L) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours > h:
                L = mid + 1
            else:
                min_speed = min(min_speed, mid)
                R = mid - 1
            
        return min_speed