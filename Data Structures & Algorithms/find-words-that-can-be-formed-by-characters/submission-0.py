class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for word in words:
            cur_word = Counter(word)
            valid = True
            for c in word:
                if not cur_word[c] <= count[c]:
                    valid = False
            if valid:
                res += len(word)

        return res
