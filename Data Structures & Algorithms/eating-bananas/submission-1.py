class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        eating_speed = R

        while L <= R:
            mid = L + (R - L) // 2

            hours = 0
            for num in piles:
                hours += math.ceil(num / mid)

            if hours <= h:
                eating_speed = mid
                R = mid - 1
            else:
                L = mid + 1

        return eating_speed