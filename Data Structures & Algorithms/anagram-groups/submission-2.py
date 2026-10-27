class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dictionary
        dic = defaultdict(list)

        # iterate over strs 
        for s in strs:
            # for each string s, sort it and add it to the dictionary
            # sorted words will have the same result
            sort = ''.join(sorted(s))
            dic[sort].append(s)
        return list(dic.values())