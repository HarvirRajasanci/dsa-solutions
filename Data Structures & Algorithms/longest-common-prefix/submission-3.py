class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        longest = max(strs)
        shortest = min(strs)

        i = 0
        while i < len(shortest) and shortest[i] == longest[i]:
            i += 1

        return shortest[:i]