class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            l = len(s)
            res += str(l) + '#' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        num = ''

        while index < len(s):
            if s[index].isdigit():
                num += s[index]
                index += 1
            if s[index] == '#':
                temp = ''
                index +=1
                end = index + int(num)
                while index < end:
                    temp += s[index]
                    index +=1
                res.append(temp)
                num = ''

        return res
