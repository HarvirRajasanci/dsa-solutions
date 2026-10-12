class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        min_hours = float("inf")

        while L <= R:
            mid = L + (R - L) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            
            if time <= h:
                min_hours = mid
                R = mid - 1
            else:
                L = mid + 1

        return min_hours