class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            num = 0
            while n > 0:
                num += (n % 10)**2
                n = n // 10
            n = num
        return n == 1