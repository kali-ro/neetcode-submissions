class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        def hasVowels(s):
            vowels = {'a', 'e', 'i', 'o', 'u'}

            if s[0] in vowels and s[-1] in vowels:
                return True
                
            return False
        
        res = []
        for q in queries:
            temp = 0
            for i in range(q[0], q[1] + 1, 1):
                if hasVowels(words[i]):
                    temp += 1
                
            res.append(temp)
        
        return res