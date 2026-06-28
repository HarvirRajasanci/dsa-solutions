class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = longest_substring = 0

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            longest_substring = max(longest_substring, len(seen))
        return longest_substring