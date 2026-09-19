class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = longest = 0

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            longest = max(longest, R - L + 1)

        return longest