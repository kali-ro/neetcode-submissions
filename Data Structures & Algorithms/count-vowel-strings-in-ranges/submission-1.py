class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        def hasVowels(s):
            vowels = {'a', 'e', 'i', 'o', 'u'}

            if s[0] in vowels and s[-1] in vowels:
                return 1
                
            return 0
        
        res = []
        prefix = [0] * (len(words) + 1)
        for i in range(1, len(prefix), 1):
            prefix[i] = prefix[i - 1] + hasVowels(words[i - 1])

        for q in queries:
            res.append(prefix[q[1] + 1] - prefix[q[0]])
        
        return res