class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_substring = 0

        L = R = 0
        while R < len(s):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            longest_substring = max(longest_substring, len(seen))
            R += 1
        return longest_substring