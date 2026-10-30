class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_counts = []
        i = 0
        while i <= n:
            count = 0
            num = i
            while num > 0:
                if num & 1 == 1:
                    count += 1
                num = num >> 1
            bit_counts.append(count)
            i += 1
        return bit_counts