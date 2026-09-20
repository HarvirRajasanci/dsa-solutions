class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = max(strs)
        shortest = min(strs)

        i = 0
        while i < len(shortest):
            if longest[i] != shortest[i]:
                break
            i += 1
        return shortest[:i]