class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        seen = {}

        L = R = 0
        while L < len(s2):
            if s2[L] not in need:
                L += 1
                continue
            R = L
            while R < len(s2) and R - L < len(s1) and s2[R] in need:
                seen[s2[R]] = 1 + seen.get(s2[R], 0)
                R += 1
            if seen == need:
                return True
            seen = {}
            L += 1
        return False
        
