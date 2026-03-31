class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res= defaultdict(list)

        for s in strs:
            count=[0]*26

            for c in s:
                count[ord(c)-ord('a')]+=1
            # list is not mustable so convert it to atuple to use as our key
            res[tuple(count)].append(s)

        return list(res.values())        