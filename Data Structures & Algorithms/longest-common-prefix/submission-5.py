class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = max(strs)
        shortest = min(strs)

        i = 0
        while i < len(shortest) and longest[i] == shortest[i]:
            i += 1
            
        return shortest[:i]