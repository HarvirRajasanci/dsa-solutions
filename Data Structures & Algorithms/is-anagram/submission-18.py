class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord('a') - ord(s[i])] += 1
            count[ord('a') - ord(t[i])] -= 1

        for num in count:
            if num != 0:
                return False
        return True
