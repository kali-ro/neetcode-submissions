class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        r = 0
        l = 0
        res = 0
        while l < len(s):
            if s[l] in window:
                while s[l] in window:
                    window.remove(s[r])
                    r += 1

            if s[l] not in window:
                window.add(s[l])
                l += 1
            res = max(res, l - r)
        return res            
