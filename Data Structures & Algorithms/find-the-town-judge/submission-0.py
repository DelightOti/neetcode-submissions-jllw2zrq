class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        hashmap = {}

        for a, b in trust:

            hashmap[a] = hashmap.get(a, 0) - 1
            hashmap[b] = hashmap.get(b, 0) + 1
        
        for person in hashmap:
            if hashmap[person] == n - 1:
                return person
        return -1


        