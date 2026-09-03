class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        L = maxf = length = 0

        for R in range(len(s)):
            window[s[R]] = 1 + window.get(s[R], 0)
            maxf = max(maxf, window[s[R]])

            while (R - L + 1) - maxf > k:
                window[s[L]] = window.get(s[L]) - 1
                if window[s[L]] == 0:
                    del window[s[L]]
                L += 1
                
            length = max(length, R - L + 1)
        return length