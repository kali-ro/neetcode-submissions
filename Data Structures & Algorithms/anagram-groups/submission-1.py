class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # sets up an array for the alpahabet
            count = [0] * 26
            for c in s:
                # use ord to get the ascii value
                count[ord(c) - ord('a')] += 1

            # convert to count to tuple as key in dict 
            res[tuple(count)].append(s)
        return list(res.values())