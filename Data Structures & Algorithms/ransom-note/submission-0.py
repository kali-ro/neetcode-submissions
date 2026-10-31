class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_mag = Counter(magazine)
        count_ran = Counter(ransomNote)

        for c in ransomNote:
            if not count_ran[c] <= count_mag[c]:
                return False

        return True